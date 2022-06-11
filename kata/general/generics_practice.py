"""
The aim of generics are to:
1. Allow functions, methods and classes to work with arguments of any type whilst
maintaining the information on the relationships between things, such as arguments and return values.
2. Better define how types can mix
"""
from typing import List, TypeVar

T = TypeVar("T")

FROM_TYPE = TypeVar("FROM_TYPE")
TO_TYPE = TypeVar("TO_TYPE")


def mapper(a: FROM_TYPE, b: TO_TYPE) -> TO_TYPE:
    print(a)
    return b


def first(container):
    return container[0]


def second(container: List[T]) -> T:
    return container[1]


# def third(container: List[T]) -> T:
#     print(container)
#     return "a"


if __name__ == "__main__":
    alphas = ["a", "b", "c"]
    print(first(alphas))

    numerics = [1, 2, 3]
    print(first(numerics))

    alphas_2: List[str] = ["v", "acv", "k"]
    print(second(alphas_2))

    bools: List[bool] = [True, True, False]
    print(second(bools))

    # 'kata/general/generics_practice.py:22: error: Incompatible return value type (got "str", expected "T")'
    # value = third(alphas)
