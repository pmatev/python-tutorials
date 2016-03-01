class ExampleException(Exception):
    pass

class NotCaughtException(Exception):
    pass

try:
    raise NotCaughtException()
except ExampleException as err:
    print('caught')
finally:
    print('finally')
