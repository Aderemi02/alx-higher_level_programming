#!/usr/bin/python3
"""
using a square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    rep a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """"
        intializing the square
        using argment:

        size: size of the square
        x: x co-ordinate
        y: y co-ordinate
        id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getting and setting size of a square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        returning the print and str rep of the square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        updating the square by assigning attributes:
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """

        if args and len(args) != 0:
            num = 0
            for i in args:
                if num == 0:
                    if i is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif num == 1:
                    self.size = i
                elif num == 2:
                    self.x = i
                elif num == 3:
                    self.y = i
                num += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """
        returning the dict rep if the sqaure
        """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
