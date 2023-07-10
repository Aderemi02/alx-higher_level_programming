#!/usr/bin/python3
"""
calculating the area of the square and also rep string
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    a square class
    """

    def __init__(self, size):
        """
        used to validate width and height
        """

        self.integer_validator("size", size)
        super().__init__(self.size, self.__size)
        self.__size = size
