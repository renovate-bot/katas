from abc import ABCMeta, abstractmethod

from kata.constants import FizzBuzzWhizz


class Rule(metaclass=ABCMeta):

    @abstractmethod
    def check(self, num):
        pass


class MultiplesOfThree(Rule):
    def check(self, num):
        if num % 3 == 0:
            return f"{FizzBuzzWhizz.FIZZ}"
        return num


class MultiplesOfFive(Rule):
    def check(self, num):
        if num % 5 == 0:
            return f"{FizzBuzzWhizz.BUZZ}"
        return num


class MultiplesOfSeven(Rule):
    def check(self, num):
        if num % 7 == 0:
            return f"{FizzBuzzWhizz.Whizz}"
        return num


class MultiplesOfThreeAndFive(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return f"{FizzBuzzWhizz.FIZZ}{FizzBuzzWhizz.BUZZ}"
        return num


class MultiplesOfThreeAndSeven(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 7 == 0:
            return f"{FizzBuzzWhizz.FIZZ}{FizzBuzzWhizz.Whizz}"
        return num


class MultiplesOfFiveAndSeven(Rule):
    def check(self, num):
        if num % 5 == 0 and num % 7 == 0:
            return f"{FizzBuzzWhizz.BUZZ}{FizzBuzzWhizz.Whizz}"
        return num


class MultiplesOfThreeAndFiveAndSeven(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            return f"{FizzBuzzWhizz.FIZZ}{FizzBuzzWhizz.BUZZ}{FizzBuzzWhizz.Whizz}"
        return num


class ContainThree(Rule):
    def check(self, num):
        if '3' in str(num):
            return f"{FizzBuzzWhizz.FIZZ}"
        return num


class ContainFive(Rule):
    def check(self, num):
        if '5' in str(num):
            return f"{FizzBuzzWhizz.BUZZ}{FizzBuzzWhizz.Whizz}"
        return num


class ContainSeven(Rule):
    def check(self, num):
        if '7' in str(num):
            return f"{FizzBuzzWhizz.FIZZ}"
        return num
