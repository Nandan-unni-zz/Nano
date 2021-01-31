class Router:

    def __init__(self):
        self.urls = []
        self.controllers = []
        self.methods = []

    def get(self, url: str, controller):
        self.urls.append(url)
        self.controllers.append(controller)
        self.methods.append('GET')

    def post(self, url: str, controller):
        self.urls.append(url)
        self.controllers.append(controller)
        self.methods.append('POST')