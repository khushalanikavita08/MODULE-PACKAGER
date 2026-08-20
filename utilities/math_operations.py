import math


def factorial(number):
    return math.factorial(number)


def compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    interest = amount - principal

    return amount, interest


def circle_area(radius):
    return math.pi * radius * radius


def rectangle_area(length, width):
    return length * width


def square_area(side):
    return side * side


def logarithm(number, base):
    return math.log(number, base)


def trigonometry(angle):
    radians = math.radians(angle)

    return {
        "sin": math.sin(radians),
        "cos": math.cos(radians),
        "tan": math.tan(radians)
    }
