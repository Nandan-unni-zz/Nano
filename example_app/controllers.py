from nanoAPI.handler import Response

def index(req):
    return Response(status=200, data={"message": "Welcome to your first Nano app"})

def create_user(req):
    print(req.data)
    return Response(status=201, data={"user": req.data})

def get_user(req):
    return Response(status=200, data={"user": "user details"})

def delete_user(req):
    return Response(status=200, data={"message": "User deleted"})
