from nano.handler import Response

def index(req):
    return Response(status=200, data={"message": "Welocome to your first Nano app"})

def create_user(req):
    print(req.data)
    return Response(status=201, data=req.data)

def get_user(req):
    return Response(status=200, data={"user": "User found"})

def delete_user(req):
    return Response(status=200, data={"message": "Deleted user"})
