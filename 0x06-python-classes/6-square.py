#!/usr/bin/python3
"""Writing a class Square that defines
a square based on 5-square.py"""


class Square:
    """a Square class with a size validation,
    calculating the area of the square"""
    def __init__(self, size=0, position=(0, 0)):
        """ an init method with an optional attribute
        size having an int type
        position, a tuple also having an int type"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getting the property of the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setting a value to the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getting the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setting the new position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    def area(self):
        """a public method to calculate the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the result of the square using #"""
        if (self.__size == 0):
            print("")
        [print("") for pos in range(self.position[1])]
        for num in range(self.__size):
            [print(" ", end="") for pos in range(self.position[0])]
            for num2 in range(self.__size):
                print("#", end="")
            print("")
