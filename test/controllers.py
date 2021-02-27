from nanoAPI.handler import Response
from .models import TestModel_A


def test_controller_1(req):
    print(req.params, req.queries)
    return Response(status=200, data={"message": "Response from test controller 1"})


def test_controller_2(req):
    print(req.params, req.queries)
    model_data = TestModel_A.find(id=req.params["id"])
    return Response(status=201, data={"model_data": model_data})


def test_controller_3(req):
    print(req.data)
    print(TestModel_A.create(req.data))
    return Response(status=200, data={"message": "Response from test controller 3"})


def test_controller_4(req):
    print(req.params, req.queries)
    return Response(status=201, data={"message": "Response from test controller 4"})
