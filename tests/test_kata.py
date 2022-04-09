from kata.fizz_buzz import iterator
from kata.rule import *


class TestRules:

    def test_fizz_buzz(self):
        assert iterator(15) == [1,
                                2,
                                'Fizz',
                                4,
                                "BuzzWhizz",
                                "Fizz",
                                "Fizz",
                                8,
                                "Fizz",
                                "Buzz",
                                11,
                                "Fizz",
                                "Fizz",
                                "Whizz",
                                "BuzzWhizz"
                                ]

    def test_should_return_fizz_when_given_9(self):
        assert MultiplesOfThree().check(9) == "Fizz"

    def test_should_return_buzz_when_given_10(self):
        assert MultiplesOfFive().check(10) == "Buzz"

    def test_should_return_whizz_when_given_21(self):
        assert MultiplesOfSeven().check(21) == "Whizz"

    def test_should_return_fizzbuzz_when_given_30(self):
        assert MultiplesOfThreeAndFive().check(30) == "FizzBuzz"

    def test_should_return_fizzbuzz_when_given_42(self):
        assert MultiplesOfThreeAndSeven().check(21) == "FizzWhizz"

    def test_should_return_buzzwhizz_when_given_70(self):
        assert MultiplesOfFiveAndSeven().check(70) == "BuzzWhizz"

    def test_should_return_fizzbuzzwhizz_when_given_105(self):
        assert MultiplesOfThreeAndFiveAndSeven().check(105) == "FizzBuzzWhizz"

    def test_should_return_fizz_when_given_13(self):
        assert ContainThree().check(13) == "Fizz"

    def test_should_return_buzzwhizz_when_given_53(self):
        assert ContainFive().check(53) == "BuzzWhizz"

    def test_should_return_fizz_when_given_17(self):
        assert ContainSeven().check(17) == "Fizz"
