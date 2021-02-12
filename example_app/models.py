from nanoAPI.db import model


class User(model.Model):
    username = model.StringType(
        'username', max_length=50, min_length=4, unique=True, required=True)
    ph_no = model.IntegerType('ph_no', max=9999999999, min=9000000000)
    is_admin = model.BooleanType('is_admin', default=False)


class User2(model.Model):
    username = model.StringType(
        'username', max_length=50, min_length=4, unique=True, required=True)
    ph_no = model.IntegerType('ph_no', max=9999999999, min=9000000000)
    is_admin = model.BooleanType('is_admin', default=False)


class User3(model.Model):
    username = model.StringType(
        'username', max_length=50, min_length=4, unique=True, required=True)
    ph_no = model.IntegerType('ph_no', max=9999999999, min=9000000000)
    is_admin = model.BooleanType('is_admin', default=False)
