from nanoAPI.utils import log

class Request:

    def __init__(self, environ):
        self.path = environ['PATH_INFO']
        self.method = environ['REQUEST_METHOD']
        self.content_length = int(environ.get('CONTENT_LENGTH', 0))
        self.data = environ['wsgi.input'].read(self.content_length).decode('utf-8')

    def __str__(self):
        return log("REQ", self.method, self.path)
