from nanoAPI.handler import Router
from .controllers import index, create_user, get_user, delete_user

router = Router()

router.get('/', index)
router.get('/user/:id', get_user)
router.post('/user', create_user)
router.get('/user/delete/:id', delete_user)
