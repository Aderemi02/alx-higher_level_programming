#!/usr/bin/python3
"""
writing a class based in 5-base_geometry.py
"""


class BaseGeometry:
    """
    an empty class
    """

    def area(self):
        """Method for the area"""

        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """method for validating the value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
