#!/usr/bin/python3
"""Write a class MyInt that inherits from int:

    *MyInt is a rebel. MyInt has == and != operators inverted
    *You are not allowed to import any module
"""


class MyInt(int):
    """This class invert the operators"""
    def __ne__(self, other):
        return not self.__eq__(other)
