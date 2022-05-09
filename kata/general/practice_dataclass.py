from dataclasses import dataclass, astuple, asdict, field


# @dataclass(frozen=True)
@dataclass
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"
    full_name: str = field(init=False, repr=True)

    # hobbies: str

    def __post_init__(self):
        self.full_name = self.first_name + " " + self.last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age})"


ahmed = Person()

# re-write __repr__
print(ahmed)

# output to expected format
print(astuple(ahmed))

print(asdict(ahmed))

# Frozen instances / immutable objects
# ahmed.age = 1111

# Compare two instances without defining __eq__
first_person = Person("Ahmed", "Besbes", 30, "Data scientist")
second_person = Person("Ahmed", "Besbes", 30, "Data scientist")

print(first_person == second_person)

# Custom attribute behaviour with the field function
# print(ahmed.full_name)
print(ahmed)
print(ahmed.full_name)


@dataclass(order=True)
class Animal:
    name: str = "aha"
    age: int = 0

    sort_index: int = field(init=False, repr=False)

    def __post_init__(self):
        self.sort_index = self.age


a1 = Animal(name="robin",age=30)
a2 = Animal(name="jack",age=50)

print(f"a1 > a2: {a1 > a2}")
