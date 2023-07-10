#!/usr/bin/python3
"""
calculating the area of the square and also rep string
"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """
    a square class
    """

    def __init__(self, size):
        """
        used to validate width and height
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.size, self.__size)

    def area(self):
        """
        this calculates the area of the rectangle
        """

        return super().area()
