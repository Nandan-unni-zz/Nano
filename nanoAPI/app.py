from nanoAPI.utils import msg, warn, err
from nanoAPI.handler import Router, Request, Response
# from gunicorn.app.base import BaseApplication
import os, sys

class nanoAPI:
    def __init__(self, port=8000, debug=True):
        # print(msg("RUN", ""))
        self.port = port
        self.debug = debug
        self.router = Router()
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
    
    def setRouter(self, base_path=None, router=None):
        for i in range(len(router.urls)): 
            router.urls[i] = base_path + router.urls[i]
        self.router.urls.extend(router.urls)
        self.router.methods.extend(router.methods)
        self.router.controllers.extend(router.controllers)
    
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
                    pass
                else:
                    print(msg("RUN", ""))
                    run_cmd = f"gunicorn main:{param} {self.gunicorn_config()}"
                    os.system(run_cmd)
                    print(msg("END", ""))
            elif command == 'create':
                if param == 'admin':
                    pass
                else:
                    pass
        except IndexError:
            print(err("ARG", "Invalid manager arguments"))
