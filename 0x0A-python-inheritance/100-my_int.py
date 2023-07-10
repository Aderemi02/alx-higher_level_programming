#!/usr/bin/python3
""" a class MyInt that inherits from int:"""


class MyInt(int):
    """
    a class that inherits from int
    """

    def __eq__(self, val):
        """give the inverted version"""

        return int.__ne__(self, val)

    def __ne__(self, val):
        """give the inverted version"""

        return int.__eq__(self, val)
