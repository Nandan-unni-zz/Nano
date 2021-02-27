# NANO : A Nano Web Framework

Nano is an Express inspired nano web framework which is under development. Currently, it has features of adding routes, controllers and sending API responses (Refer the [example blog app](https://github.com/NandanunniAS/Nano-Blog-App) for reference). Defining models with custom field types is also available but is under development.

**Status** : Under developement
<br />

### To run example app

```bash
$ pip3 install -r requirements.txt

$ python3 main.py run:<appname>
```

## Documentation

**Step 1**: Install nanoAPI and create folder structure
```bash
$ pip3 install nanoAPI

$ touch models.py
$ touch controllers.py
$ touch routes.py
$ touch main.py
```

<br />

**Step 1**: Install nanoAPI and create folder structure
```python
# models.py
from nanoAPI.db import model

class User(model.Model):
    username = model.StringType('username', max_length=50, min_length=4, unique=True, required=True)
    # define your model here
```

<br />

**Step 2**: Define your controllers
```python
# controllers.py
from nanoAPI.handler import Response

def index(req):
    # define your controller here
    return Response(status=200, data={"msg": "message"})
```

<br />

**Step 3**: create a router and assign controllers with routes
```python
# routes.py
from nanoAPI.handler import Router
from .controllers import index

router = Router()
router.get("/", index)
```

<br />

**Step 4**: create nanoAPI app and assemble your router and models
```python
# main.py
from nanoAPI import nanoAPI, run
from .routes import router
from .models import User

api = nanoAPI()

api.set_router('/api', router)
api.set_models(User)

run(api)
```

<br />

**Step 5**: Boot your models to db and run the server
```bash
$ python3 main.py run:db
$ python3 main.py run:api
```


Refer the [example blog app](https://github.com/NandanunniAS/Nano-Blog-App) for folder structure. Working on a better documentation
