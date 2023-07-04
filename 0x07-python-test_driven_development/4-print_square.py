#!/usr/bin/python3
"""Printing a square using the character #"""


def print_square(size):
    """A function that prints a square with the character #
    using an arguement that specfies the size of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for new in range(size)]
        print("")
