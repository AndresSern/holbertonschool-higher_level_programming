#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """Initialize a class with init"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position;

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    "Defining the square"""
    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            count = 1
            while(count <= self.__size):
                if self.__position[1] <= 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
                count += 1
