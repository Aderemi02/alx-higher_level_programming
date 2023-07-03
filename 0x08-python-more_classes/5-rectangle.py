#!/usr/bin/python3
"""This is a module that defines a rectangle"""


class Rectangle:
    """ This defines a rectangle"""

    def __init__(self, width=0, height=0):
        """This initializes the instance with arguements of:

        Width: the width of the rectangle.
        Height: the height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        this returns the value of the width
        Returns: width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        This sets the value of the width with the arguement:
        value: value of the width of the rectangle.

        Raises:
        TypeError: "width must be an integer". if value is not integer
        ValueError: "width must be >= 0". if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        this returns the value of the height
        Returns: height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        This sets the value of the height with the arguement:
        value: value of the height of the rectangle.

        Raises:
        TypeError: "height must be an integer". if value is not integer
        ValueError: "height must be >= 0". if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """ this returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ string rep of the rectangle using #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rec = ""

        for new in range(self.__height):
            rec += ("#" * self.__width) + "\n"
        return rec[0:-1]

    def __repr__(self):
        """this returns the string rep of instance"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """this prints a message that shows an instance is deleted"""

        print("Bye rectangle...")
