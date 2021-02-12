from nanoAPI.handler import Router
from .controllers import (
    test_controller_1,
    test_controller_2,
    test_controller_3,
    test_controller_4
)

test_router = Router()

test_router.get('/', test_controller_1)
test_router.get('/test/:id', test_controller_2)
test_router.post('/test', test_controller_3)
test_router.get('/test/four/:id', test_controller_4)
