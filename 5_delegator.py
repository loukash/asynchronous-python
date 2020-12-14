def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, *kwargs)
        g.send(None)
        return g
    return inner


class MyException(Exception):
    pass


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except (StopIteration, MyException):
            print('Catch My Exception')
            break
        else:
            print('**************', message)

    return 'Returned string from subgen()'


@coroutine
def delegator(sub):
    # while True:
    #     try:
    #         data = yield
    #         sub.send(data)
    #     except MyException as e:
    #         sub.throw(e)
    result = yield from sub
    print(result)

