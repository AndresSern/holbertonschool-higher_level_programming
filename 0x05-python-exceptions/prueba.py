#!/usr/bin/python3
"""
 * safe_print_integer - Function that prints an integer with "{:d}".format().
 *
 * @value: value can be any type (integer, string, etc.)
 *
 * Return: True if value has been correctly printed (it means
 *         the value is an integer)
 *
 """
a = 10
b =
try:
    # condition for checking for negative values
    if a < 0 or b < 0:
        # raising exception using raise keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter valid integer value")

