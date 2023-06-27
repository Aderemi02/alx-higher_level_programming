#!/usr/bin/python3
"""writing a class Square that defines square by: 0-square.py"""


class Square:
    """this s a class square
    in this class we will be having an init method with a size attribute"""
    def __init__(self, size):
        """Using the init method with an argument.
        the parameter is called size with an (int) type"""
        self.__size = size
