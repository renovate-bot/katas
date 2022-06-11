class BingoCage:
    def __init__(self, items):
        self._item = list(items)

    def __call__(self):
        try:
            return self._item.pop()
        except IndexError as exc:
            raise LookupError("pick up from empty BingoCage!") from exc


def exmaple_for_enumerate():
    with open("data_for_enumerate.txt", "r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            print(f"No.{index}: {line}")


def example_for_zip():
    l1 = [1, 2, 3, 4]
    l2 = ["a", "b", "c", "d"]
    zipped_l = zip(l1, l2)
    for i, j in zipped_l:
        print(f"{i},{j}")
    print(list(zipped_l))


def accept_params(*arg, **kwargs):
    print(arg, kwargs)


def example_for_unpack():
    some_args = range(3)
    print(type(some_args))
    more_args = {
        "arg1": "ONE",
        "arg2": "TWO"
    }
    print(type(more_args))

    def show_arg(arg1, arg2, arg3="THREE"):
        print(arg1, arg2, arg3)

    # unpack a sequence
    show_arg(*some_args)
    # unpack a dict
    show_arg(**more_args)


def example_for_function_description():
    example_for_unpack.description = "what a silly function"
    print(example_for_unpack.__name__)
    print(example_for_unpack.__class__)
    print(example_for_unpack.description)


if __name__ == "__main__":
    # exmaple_for_enumerate()
    #
    # example_for_zip()
    #
    # accept_params(1, 2, 3, 4, a=1, b=2)
    #
    # example_for_unpack()
    #
    # example_for_function_description()

    bingo = BingoCage(range(3))
    print(bingo())
    print(callable(bingo))
