#!/usr/bin/python3
"""
writing a class based in 5-base_geometry.py
"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


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
