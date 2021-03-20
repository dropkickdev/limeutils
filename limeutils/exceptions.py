

class ValidationError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(message)


class RedisError(Exception):
    pass


