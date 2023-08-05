from concurrent.futures import CancelledError
import logging
import os

from aiohttp.web import FileResponse, HTTPFound, Response

from flamingo.core.data_model import ContentSet, Content
from flamingo.core.utils.pprint import pformat


class History:
    def __init__(self):
        self.clear()

    def clear(self):
        self.history = []
        self.contents = ContentSet()

    def append(self, item):
        self.history.append(item)

        if isinstance(item, Content):
            self.contents.add(item)

    def __iter__(self):
        return self.history.__iter__()

    def __repr__(self):
        return pformat(self.history)


class ContentExporter:
    def __init__(self, context, history):
        self.context = context
        self.history = history

        self.static_dirs = [
            os.path.dirname(i)
            for i in self.context.templating_engine.find_static_dirs()
        ]

        self.logger = logging.getLogger('flamingo.server.exporter')

    def clear(self):
        self.logger.debug('clearing history...')
        self.history.clear()

    def resolve(self, request_path):
        # post build layers
        # static
        # media
        # content
        # pre build layers

        request_path = request_path[1:]

        if not request_path:
            request_path = 'index.html'

        self.logger.debug("request_path: '%s'", request_path)

        def _resolve_paths(paths):
            for path in paths[::-1]:
                path = os.path.join(path, request_path)

                if not os.path.exists(path):
                    continue

                if os.path.isdir(path):
                    index_path = os.path.join(path, 'index.html')

                    if os.path.exists(index_path):
                        return index_path

                return path

            return ''

        # post build layers
        path = _resolve_paths(self.context.settings.POST_BUILD_LAYERS)

        if path:
            self.logger.debug("handled as post build layer: '%s'", path)

            return path

        # static files
        path = _resolve_paths(self.static_dirs)

        if path:
            self.logger.debug("handled as static file: '%s'", path)

            return path

        # media files
        media_url = '/' + request_path

        contents = self.context.contents.filter(
            media__passes=lambda m: m and m.filter(url=media_url).exists())

        if contents.exists():
            media_contents = contents.last()['media']
            media_content = media_contents.filter(url=media_url).last()

            self.context.plugins.run_plugin_hook('render_media_content',
                                                 media_content)

            self.logger.debug("handled as media file: '%s'",
                              media_content['path'])

            return os.path.join(self.context.settings.CONTENT_ROOT,
                                media_content['path'])

        # content
        contents = self.context.contents.filter(output=request_path)
        content = None

        if contents.exists():
            content = contents.last()

        else:  # index.html
            contents = self.context.contents.filter(
                output=os.path.join(request_path, 'index.html')
            )

            if contents.exists():
                content = contents.last()

        if content:
            self.context.plugins.run_plugin_hook('render_content', content)

            self.logger.debug("handled as content: '%s'",
                              content['path'] or content)

            return content

        # pre build layers
        path = _resolve_paths(self.context.settings.PRE_BUILD_LAYERS)

        if path:
            self.logger.debug("handled as pre build layer: '%s'", path)

            return path

    async def __call__(self, request):
        def _404():
            self.logger.debug('404: not found')

            return Response(text='404: not found', status=404)

        def gen_response(path):
            content = self.resolve(path)

            # 404
            if not content:
                return _404()

            # file response
            if isinstance(content, str):
                if(not os.path.exists(content) or
                   os.path.isdir(content)):

                    return _404()

                return FileResponse(content)

            # content response
            if content['redirect']:
                raise HTTPFound(content['redirect'])

            try:
                output = self.context.render(content)
                self.history.append(content)

            except Exception as e:
                self.context.logger.error(e, exc_info=True)

                return Response(text='500: rendering error', status=500)

            return Response(text=output, content_type='text/html')

        try:
            response = await request.app['rpc'].loop.run_in_executor(
                request.app['rpc'].worker_pool.executor,
                gen_response,
                request.path
            )

        except CancelledError:
            response = Response(text='499: Client Closed Request', status=499)

        except Exception as e:
            if isinstance(e, HTTPFound):  # redirects
                raise

            self.context.logger.error(e, exc_info=True)

            response = Response(text='500: Internal Error', status=500)

        return response
