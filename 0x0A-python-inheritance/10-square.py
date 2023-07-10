#!/usr/bin/python3
"""
calculating the area of the square and also rep string
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square class
    """

    def __init__(self, size):
        """
        used to initialize the size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
