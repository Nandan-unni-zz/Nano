from nanoAPI.utils import msg, warn, err
from nanoAPI.handler import Router, Request, Response
from nanoAPI.db import DB
# from gunicorn.app.base import BaseApplication
import os
import sys


class nanoAPI:

    def __init__(self, port=8000, debug=True):
        # print(msg("RUN", ""))
        self.port = port
        self.debug = debug
        self.router = Router()
        self.database = DB()
        self.APP_DIR = os.path.abspath(os.getcwd())
        # super().__init__()
        # self.cfg.set('loglevel', 'warning')

    def __call__(self, environ, start_response):
        response = self.request_handler(environ)
        start_response(response.status_msg, response.headers)
        return [bytes(response.data, 'utf-8')]

    # def __del__(self):
    #     self.restarted = True

    def request_handler(self, request_environ):
        request = Request(request_environ)
        response = Response()
        print(request)
        res_controller, request = self.router.search_route(request)
        if res_controller:
            response = res_controller(request)
        else:
            response = Response(status=404)
            print(
                err("REQUEST", f"URL '{request.url}' not found in server router"))
        if not isinstance(response, Response):
            response = Response(status=500)
            print(err("RESPONSE", "The controller must return a Response object"))
            print(response)
            raise TypeError(
                warn("The controller must return a HTTP Response object"))
        print(response)
        return response

    def setRouter(self, base_path=None, router=None):
        for i in range(len(router.routes)):
            router.routes[i]['url'] = base_path + router.routes[i]['url']
        self.router.routes.extend(router.routes)

    def setModels(self, *args):
        self.database.set_models(*args)

    def gunicorn_config(self):
        cmd = ""
        cmd = cmd + f"-b 127.0.0.1:{self.port}"
        cmd = cmd + (" --reload" if self.debug else "")
        cmd = cmd + " --log-level warning"
        return cmd

    def run(self):
        # arguments = ['run:app', 'run:db', 'create:testuser', 'create:admin']
        try:
            arg = sys.argv[1]
            command = arg.split(':')[0]
            param = arg.split(':')[1]
            if command == 'run':
                if param == 'db':
                    print(msg("RUN", "DataBase"))
                    self.database.boot()
                    print(msg("END", "DataBase"))
                else:
                    print(msg("RUN", "Server"))
                    run_cmd = f"gunicorn main:{param} {self.gunicorn_config()}"
                    os.system(run_cmd)
                    print(msg("END", "Server"))
            elif command == 'create':
                if param == 'admin':
                    pass
                else:
                    pass
        except IndexError:
            print(err("ARG", "Invalid manager arguments"))
