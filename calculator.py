#https://github.com/vijha4951/Lab-11-SJ-KK
# Partner 1: Sannvi Jha
# Partner 2: Kaushik

import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take square root of a negative number")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except (TypeError, ValueError):
        raise ValueError("Invalid hypotenuse arguments")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


def mul(a, b):
    return multiply(a, b)


def div(a, b):
    return divide(a, b)


def exp(a, b):
    return exponent(a, b)

