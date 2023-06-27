#!/usr/bin/python3
"""Writing a class Square that defines
a square based on 1-square.py"""


class Square:
    """a Square class with a size validation"""
    def __init__(self, size=0):
        """ an init method with an optional attribute
        size having an int type"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
