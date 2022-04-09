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


class MultiplesOfSeven(Rule):
    def check(self, num):
        if num % 7 == 0:
            return "Whizz"
        return num


class MultiplesOfThreeAndFive(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        return num


class MultiplesOfThreeAndSeven(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 7 == 0:
            return "FizzWhizz"
        return num


class MultiplesOfFiveAndSeven(Rule):
    def check(self, num):
        if num % 5 == 0 and num % 7 == 0:
            return "BuzzWhizz"
        return num


class MultiplesOfThreeAndFiveAndSeven(Rule):
    def check(self, num):
        if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            return "FizzBuzzWhizz"
        return num


class ContainThree(Rule):
    def check(self, num):
        if '3' in str(num):
            return "Fizz"
        return num


class ContainFive(Rule):
    def check(self, num):
        if '5' in str(num):
            return "BuzzWhizz"
        return num


class ContainSeven(Rule):
    def check(self, num):
        if '7' in str(num):
            return "Fizz"
        return num
