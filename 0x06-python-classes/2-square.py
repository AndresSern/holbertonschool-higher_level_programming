#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """Initialize a class with init"""
    def __init__(self, size=0):
            """ If Not a Integer Raise an error"""
        if type(size) is not int:
            raise TypeError
            """ If size < 0 Raise an error"""
        elif size < 0:
            raise ValueError
        self.__size = size
