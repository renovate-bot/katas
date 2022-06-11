import inspect
from typing import TypeVar
from inspect import getmembers

FROM_OBJ = TypeVar("FROM_OBJ")
TO_OBJ = TypeVar("TO_OBJ")


class Mapper:

    def __init__(self, from_obj: FROM_OBJ, to_obj: TO_OBJ, rules=None):
        self.from_obj = from_obj
        self.to_obj = to_obj
        self.rules = rules

    # pylint: disable=bare-except
    def map(self):
        target_obj = self.to_obj()
        for key, value in self.get_attr().items():

            try:
                value_from_obj = getattr(self.from_obj, key)
            except:
                value_from_obj = None

            if value_from_obj and self.rules and key in self.rules:
                value_from_obj = self.rules.get(key)(value_from_obj)

            setattr(target_obj, key, value_from_obj or value)
        return target_obj

    def get_attr(self):
        return {k: v for k, v in getmembers(self.to_obj(), lambda item: not callable(item)) if not k.startswith("__")}


class Origin:
    def __init__(self, key: str = ""):
        self.key = key


class Target:
    def __init__(self, key: str = ""):
        self.key = key


class A:
    def __init__(self):
        self.name = "just_name"
        self.nest = Origin("nest-key")


class B:

    def __init__(self):
        self.name: str = None
        self.age: int = 10
        self.nest: Target = None


if __name__ == "__main__":
    # m = Mapper(A(), B, {"name": lambda x: x.upper()})
    # print(result := m.map())
    # print(result.name)
    # print(result.age)
    # print(result.nest)
    b = B()
    o = inspect.getclasstree(b)
    print(o)
    # attrs = [i for i in dir(b) if not i.startswith("__")]
