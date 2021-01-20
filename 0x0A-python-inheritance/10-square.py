#!/usr/bin/python3
"""
Class Called BaseGeometry
"""


class BaseGeometry:
    """This is a class called BaseGeometry"""

    def area(self):
        """This Function Raise an Error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be a greater than 0")


class Rectangle(BaseGeometry):
    """This Class called Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This is the Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This function is the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ This function return to a descripcion about this class"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """This class is Square that inherits from Rectangle"""

    def __init__(self, size):
        """This is the instantiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
