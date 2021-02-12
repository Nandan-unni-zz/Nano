# main.py for example app
from nanoAPI import nanoAPI
from example_app.routes import router
from example_app.models import User, User2, User3

api = nanoAPI()
api.port = 8000
api.debug = True

api.setRouter('/api', router)
api.setModels(User, User2, User3)

api.run()
