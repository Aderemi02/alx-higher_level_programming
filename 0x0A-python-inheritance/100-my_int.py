#!/usr/bin/python3
""" a class MyInt that inherits from int:"""


class Myint:
    """
    a class that inherits from int
    """

    def __pos__(self, other):
        return int.__neg__(self, other)

    def __neg__(self, other):
        return int.__pos__(self, other)
