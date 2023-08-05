from modutils.hashutils import sha256_pattern

class sha256:
    name = 'sha256'

    def __init__(self, value):
        value_str = str(value)
        self.__value__ = value_str if sha256_pattern.match(value_str) else None
        if not self.__value__:
            raise TypeError(f'{value!r} is not a valid sha256 type')

    def __str__(self):
        return self.__value__.lower()

    def __eq__(self, value):
        if self.__value__.lower() == sha256(value).__value__.lower():
            return True
        return False

