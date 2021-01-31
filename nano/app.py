from nano.utils import msg, warn, err
from nano.handler import Router, Request, Response
import os

class Nano:
    def __init__(self):
        print(msg("RUN", ""))
        self.router = Router()
        self.APP_DIR = os.path.abspath(os.getcwd())

    def __call__(self, environ, start_response):
        response = self.request_handler(environ)
        start_response(response.status_msg, response.headers)
        return [bytes(response.data, 'utf-8')]

    def __del__(self):
        print(msg("END", ""))

    def request_handler(self, request_environ):
        request = Request(request_environ)
        response = Response()
        found_url = False
        print(request)
        for i in range(len(self.router.urls)):
            if request.path == self.router.urls[i] and request.method == self.router.methods[i]:
                found_url = True
                response = self.router.controllers[i](request)
        if not found_url:
            response = Response(status=404)
            print(err("REQUEST", f"URL '{request.path}' not found in server router"))
        if not isinstance(response, Response):
            response = Response(status=500)
            print(err("RESPONSE", "The controller must return a Response object"))
            print(response)
            raise TypeError(warn("The controller must return a HTTP Response object"))
        print(response)
        return response
