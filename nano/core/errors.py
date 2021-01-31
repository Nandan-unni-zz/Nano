class _BaseError(Exception):
    pass

class ResponseTypeError(_BaseError):
    pass

class DBError(_BaseError):
    pass
