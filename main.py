# main.py for test

from nanoAPI import nanoAPI
from test.routes import test_router
from test.models import TestModel_A, TestModel_B, TestModel_C

test_api = nanoAPI()
test_api.port = 8000
test_api.debug = True

test_api.setRouter('/nano', test_router)
test_api.setModels(TestModel_A, TestModel_B, TestModel_C)

test_api.run()

# python3 main.py run:test_api
