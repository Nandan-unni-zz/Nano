class _BaseType():
    def __init__(self, model_type: str, name: str, unique: bool, required: bool):
        self.model_type = model_type.lower().capitalize()
        self.name = name.lower()
        self.unique = 'UNIQUE ' if unique else ''
        self.required = 'NOT NULL ' if required else ''  # Default : False
        self.base_cmd = f"{self.name} {model_type} {self.required}{self.unique}"


class IntegerType(_BaseType):
    def __init__(self, name=None, max=10000000, min=-10000000, unique=False, required=False, default=None):
        super().__init__('INTEGER', name, unique, required)
        self.check = f"CHECK ({self.name} < {max} AND {self.name} > {min})"
        self.default = f"DEFAULT {default if default else 'NULL'} "
        self.command = self.base_cmd + self.default + self.check


class StringType(_BaseType):
    def __init__(self, name=None, max_length=None, min_length=0, unique=False, required=False, default=None):
        super().__init__('TEXT', name, unique, required)
        self.default = f"DEFAULT {default if default else 'NULL'} "
        self.check = f"CHECK (length({self.name}) < {max_length} AND length({self.name}) > {min_length})"
        self.command = self.base_cmd + self.check


class BooleanType(_BaseType):
    def __init__(self, name=None, unique=False, required=False, default=None):
        super().__init__('INTEGER', name, unique, required)
        self.default = f"DEFAULT {1 if default else 0} "
        self.command = self.base_cmd + self.default


class EmailType(_BaseType):
    def __init__(self, name: str, unique: bool, required: bool):
        super().__init__('TEXT', name, unique, required)
        self.command = self.base_cmd


class LinkType(_BaseType):
    def __init__(self, name: str, unique: bool, required: bool):
        super().__init__('TEXT', name, unique, required)
        self.command = self.base_cmd
