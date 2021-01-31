class _BaseType():
    def __init__(self, model_type, name, unique, required, default):
        self.name = str(name).lower()
        self.unique = 'UNIQUE ' if unique else ''
        self.required = 'NOT NULL ' if required else ''  # Default : False
        self.base_cmd = f"{self.name} {model_type} {self.required}{self.unique}"


class IntegerType(_BaseType):
    def __init__(self, name="", max=10000000, min=-10000000, unique=False, required=False, default=None):
        super().__init__('INTEGER', name, unique, required, default)
        self.check = f"CHECK ({self.name} < {max} AND {self.name} > {min})"
        self.default = f"DEFAULT {default if default else 'NULL'} "
        self.command = self.base_cmd + self.default + self.check


class StringType(_BaseType):
    def __init__(self, name="", max_length=None, min_length=0, unique=False, required=False, default=None):
        super().__init__('TEXT', name, unique, required, default)
        self.default = f"DEFAULT {default if default else 'NULL'} "
        self.check = f"CHECK (LEN({self.name}) < {max_length} AND LEN({self.name}) > {min_length})"
        self.command = self.base_cmd + self.check


class BooleanType(_BaseType):
    def __init__(self, name="", unique=False, required=False, default=None):
        super().__init__('INTEGER', name, unique, required, default)
        self.default = f"DEFAULT {1 if default else 0} "
        self.command = self.base_cmd + self.default

