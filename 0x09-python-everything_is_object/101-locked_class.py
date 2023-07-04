#!/usr/bin/python3
"""a mmethod that prevent user from creating new instance attribute"""


class LockedClass:
    __slots__ = ["first_name"]

    def __init__(self):
        """initializes the class"""
        pass
