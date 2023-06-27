#!/usr/bin/python3
"""Writing a class Square that defines
a square based on 2-square.py"""


class Square:
    """a Square class with a size validation,
    calculating the area of the square"""
    def __init__(self, size=0):
        """ an init method with an optional attribute
        size having an int type"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

def area(self):
    """a public method to calculate the area of the square"""
    return (self.__size * self.__size)
