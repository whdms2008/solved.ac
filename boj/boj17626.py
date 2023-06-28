from sys import stdin
from math import sqrt


def is_square(n):
    if n < 0:
        return False
    return sqrt(n).is_integer()


def answer(n):
    if is_square(n):
        return 1

    squares = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]

    for square in squares:
        if is_square(n - square):
            return 2

    for square1 in squares:
        for square2 in squares:
            if is_square(n - square1 - square2):
                return 3

    return 4


print(answer(int(stdin.readline())))
