#!/usr/bin/python3
""" a class MyInt that inherits from int:"""


class Myint(int):
    """
    a class that inherits from int
    """

    def __eq__(self, val):
        return int.__ne__(self, val)

    def __ne__(self, val):
        return int.__eq__(self, val)
