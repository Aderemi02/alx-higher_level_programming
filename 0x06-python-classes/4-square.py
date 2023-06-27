#!/usr/bin/python3
"""Writing a class Square that defines
a square based on 3-square.py"""


class Square:
    """a Square class with a size validation,
    calculating the area of the square"""
    def __init__(self, size=0):
        """ an init method with an optional attribute
        size having an int type"""
        self.size = size

    @property
    def size(self):
        """getting the property of the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setting a value to the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a public method to calculate the area of the square"""
        return (self.__size * self.__size)
