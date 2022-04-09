from abc import ABCMeta, abstractmethod


class Rule(metaclass=ABCMeta):

    @abstractmethod
    def check(self, num):
        pass


class MultiplesOfThree(Rule):
    def check(self, num):
        if num % 3 == 0:
            return "Fizz"
        return num


class MultiplesOfFive(Rule):
    def check(self, num):
        if num % 5 == 0:
            return "Buzz"
        return num


class MultiplesOfFiveAndThree(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        return num
