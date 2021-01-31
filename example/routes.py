from main import api
from .controllers import index, create_user, get_user, delete_user

api.router.get("/", index)
api.router.get("/user", get_user)
api.router.post("/user/create", create_user)
api.router.get("/user/delete", delete_user)
