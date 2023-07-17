#!/usr/bin/python3
"""
a class rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    a rectangle inheriting from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing the rectangle with arguments:
        width: the width of the rctangle
        height: height of the rectangle
        x: the x co-ordinate of the rectangle
        y: y co-ordinate of the rectangle
        id: the id of the rectangle
        Errors:
        TypeError:
        when either of the height or wigth is not an integer
        when either of x or y is not an integer
        ValueError:
        when width or height is less than or equal to 0
        when x or y is less than 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        setting and getting width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        setting and getting height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        setting and getting x co-ordinate
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        setting and getting y co-ordinate
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculating the area of the rectanle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        printing out the rectangle
        using the # character
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for num3 in range(self.y)]

        for num in range(self.__height):
            [print(" ", end="") for num4 in range(self.x)]
            [print("#", end="") for num2 in range(self.__width)]
            print("")

    def __str__(self):
        """
        returning
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        assigning argumrnt to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """

        if args and len(args) != 0:
            num = 0
            for i in args:
                if num == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif num == 1:
                    self.width = i
                elif num == 2:
                    self.height = i
                elif num == 3:
                    self.x = i
                elif num == 4:
                    self.y = i
                num += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = k
                elif j == "width":
                    self.width = k
                elif j == "height":
                    self.height = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """
        Returning the dictionary rep of a rectangle
        """

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
