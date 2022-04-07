def iterator(num):
    return [fizz_buzz(i) for i in range(1, num + 1)]


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


if __name__ == "__main__":
    print(*iterator(100), sep="\n")
