from nanoAPI.handler import Response


def test_controller_1(req):
    print(req.params, req.queries)
    return Response(status=200, data={"message": "Response from test controller 1"})


def test_controller_2(req):
    print(req.params, req.queries)
    return Response(status=201, data={"message": "Response from test controller 2"})


def test_controller_3(req):
    print(req.params, req.queries)
    return Response(status=200, data={"message": "Response from test controller 3"})


def test_controller_4(req):
    print(req.params, req.queries)
    return Response(status=201, data={"message": "Response from test controller 4"})
