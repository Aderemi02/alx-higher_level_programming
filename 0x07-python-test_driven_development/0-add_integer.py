#!/usr/bin/python3
"""The addition function"""


def add_integer(a, b=98):
    """This adds two integers a and b
    returns the sum of the integers
    raises error if either of the integer is a non-integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return c
