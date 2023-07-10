#!/usr/bin/python3
""" a class MyInt that inherits from int:"""


class Myint:
    """
    a class that inherits from int
    """

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
