def my_decorator(arg):
    def inner_decorator(func):
        print("I have arg now")

        def wrapped(*args, **kwargs):
            print('before function')
            response = func(*args, **kwargs)
            print('after function')
            return response

        print('decorating', func, 'with argument', arg)
        return wrapped

    return inner_decorator


@my_decorator('foo')
def my_function(a, b):
    print('in function')
    return a + b


if __name__ == "__main__":
    print(my_function(1, 2))

    # print("--------------------")
    #
    # dec_with_arg = my_decorator('foo')
    #
    #
    # @dec_with_arg
    # def new_function(a, b):
    #     print("in function")
    #     return a + b
    #
    # print(new_function(1, 2))
