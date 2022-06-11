"""
"/" : index()
"/user": get_user()

"""


def route(arg):
    def my_dec(func):
        def wrapped(*args, **kwargs):
            print(f"args and kwargs of {func}, args: {args}, kwargs: {kwargs}")
            print(f"func:{func} will handle requests from {arg}")

        return wrapped

    return my_dec


@route("/")
def index(event, context):
    print(event, context)


@route("/user")
def get_user():
    pass


if __name__=="__main__":
    index(1, 2)
