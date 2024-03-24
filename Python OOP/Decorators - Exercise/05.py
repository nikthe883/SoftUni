def type_check(type):

    def decorator(function):

        def wrapper(params):
            if not isinstance(params, type):
                return "Bad Type"
            else:
                return function(params)
        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
