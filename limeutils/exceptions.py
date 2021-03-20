

class ValidationError(Exception):
    def __init__(self, message='', literal: list = None):
        if literal:
            literal = literal and [f'"{i}"' for i in literal] or []
            items = literal and ' or '.join(literal) or ''
            self.message = message or f'Arguments can only be: {items}.'
        else:
            self.message = message or 'Arguments must use the correct value or selection of values.'
        super().__init__(self.message)


class RedisError(Exception):
    pass


