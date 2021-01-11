#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ Class To Define a Rectangle with withd and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
