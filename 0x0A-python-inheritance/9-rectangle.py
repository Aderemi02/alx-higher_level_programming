#!/usr/bin/python3
"""
writing a class based in 5-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a rectangle class
    """

    def __init__(self, width, height):
        """
        used to validate width and height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        this calculates the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        string rep of the class
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
