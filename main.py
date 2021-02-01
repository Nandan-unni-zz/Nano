# main.py for example app
from nanoAPI import nanoAPI
from example_app.routes import router

api = nanoAPI()

api.setRouter('/api', router)

api.run()
