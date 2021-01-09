#!/usr/bin/python3
"""
This is the function about  4_print_square.py
"""


def print_square(size):
    """This function prints a square with the carachter #, size >= 0"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
