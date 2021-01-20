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
        """ Check if the value is a number positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This Class called Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This is the Instantiation of a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
