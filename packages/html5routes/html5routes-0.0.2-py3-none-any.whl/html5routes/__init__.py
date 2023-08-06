# -*- coding: utf-8 -*-
from paste import fileapp


def filter_app_factory(app, global_conf, **kwargs):
    return HTML5RoutesMiddleware(app, kwargs['index'])


class HTML5RoutesMiddleware(object):

    def __init__(self, app, index):
        self.app = app
        self.index = index

    def __call__(self, environ, start_response, exc_info=None):

        captured = []
        def capturing_start_response(status, headers, exc_info=None):
            if exc_info is not None:
                raise exc_info[0].with_traceback( exc_info[1], exc_info[2])
            captured[:] = [status, headers, exc_info]

        # We are calling the enclosed app with our own start_response
        # to 'look ahead' if the response is a 404 or not
        # the captured info is used in the regular start_response
        app_iter = self.app(environ, capturing_start_response)

        # When there was a 404, we serve the index file
        # that knows how to handle the html5 route
        if captured[0].startswith('404'):
            fa = fileapp.FileApp(self.index)
            return fa(environ, start_response)

        start_response(*captured)
        return app_iter

