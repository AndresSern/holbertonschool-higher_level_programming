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
            raise TypeError(name + " name must be an integer")
        if value <= 0:
            raise ValueError(name + " must be a greater than 0")

