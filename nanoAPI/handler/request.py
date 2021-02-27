from nanoAPI.utils import log, parse_route
import json


class Request:

    def __init__(self, environ):
        self.url = environ['PATH_INFO']
        self.method = environ['REQUEST_METHOD']
        self.params = {}
        self.queries = parse_route(
            f"{self.url}?{environ['QUERY_STRING']}")['queries']
        self.content_length = int(environ.get('CONTENT_LENGTH', 0))
        self.data = json.loads(environ['wsgi.input'].read(self.content_length).decode('utf-8'))

    def __str__(self):
        return log("REQ", self.method, self.url)
