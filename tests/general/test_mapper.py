from typing import List

from kata.general.mapper import Mapper


class Origin:
    def __init__(self, key: str = ""):
        self.key = key


class Target:
    def __init__(self, key: str = ""):
        self.key = key


class A:
    def __init__(self, name: str):
        self.name = name
        self.nest = Origin("nest-key")
        self.nests = [Origin("nest-list")]


class B:

    def __init__(self):
        self.name = ""
        self.age = 10
        self.nest: Target = None
        self.nests: List[Target] = None


class TestMapper:

    # pylint: disable=attribute-defined-outside-init
    def setup_method(self):
        self.from_obj = A("test")

    def test_should_map_obj_with_unmap_key_in_to_obj(self):
        mapper = Mapper(self.from_obj, B)
        to_obj = mapper.map()

        assert to_obj.name == "test"
        assert to_obj.age == 10

    def test_should_map_obj_with_lambda_for_map_key(self):
        mapper = Mapper(self.from_obj, B, {
            "name": (lambda x: x.upper())
        })
        to_obj = mapper.map()

        assert to_obj.name == "TEST"

    # def test_should_map_obj_with_nest_obj(self):
    #     mapper = Mapper(self.from_obj, B)
    #
    #     to_obj = mapper.map()
    #
    #     assert isinstance(to_obj.nest, Target)
    #     assert to_obj.nest.key == self.from_obj.nest.key
