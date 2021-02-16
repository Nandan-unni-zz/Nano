# main.py for test

from nanoAPI import nanoAPI, run
from test.routes import test_router
from test.models import TestModel_A, TestModel_B, TestModel_C

test_api = nanoAPI()
test_api.port = 6060
test_api.debug = True

test_api.set_router('/nano', test_router)
test_api.set_models(TestModel_A, TestModel_B, TestModel_C)

run(test_api)

# python3 main.py run:test_api
