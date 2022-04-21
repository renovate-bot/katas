# Standard decorator
def my_decorator(func):
    print("Some one call this function, I need to do sth before it.")

    def wrapped(*args, **kwargs):
        print('before function')
        response = func(*args, **kwargs)
        print('after function')
        return response

    print('decorating', func)
    return wrapped


@my_decorator
def my_function(a, b):
    print('in function')
    return a + b


print(my_function(1, 2))


my_function = my_decorator(my_function)
print(my_function(1, 2))
