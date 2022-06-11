from kata.rule import ContainSeven, ContainFive, ContainThree,\
    MultiplesOfThreeAndFiveAndSeven, MultiplesOfFiveAndSeven,\
    MultiplesOfThreeAndSeven, MultiplesOfThreeAndFive,\
    MultiplesOfSeven, MultiplesOfFive, MultiplesOfThree


def iterator(num):
    return [FizzBuzz().check(i) for i in range(1, num + 1)]


def get_rules():
    return (
        ContainSeven,
        ContainFive,
        ContainThree,
        MultiplesOfThreeAndFiveAndSeven,
        MultiplesOfFiveAndSeven,
        MultiplesOfThreeAndSeven,
        MultiplesOfThreeAndFive,
        MultiplesOfSeven,
        MultiplesOfFive,
        MultiplesOfThree,
    )


class FizzBuzz:

    def __init__(self):
        self.rules = get_rules()

    def check(self, num):
        for rule in self.rules:
            result = rule().check(num)
            if isinstance(result, str):
                return result
        return num


if __name__ == "__main__":
    print(*iterator(100), sep="\n")
