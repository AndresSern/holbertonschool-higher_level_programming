#!/usr/bin/python3
"""
 * safe_print_integer - Function that prints an integer with "{:d}".format().
 *
 * @value: value can be any type (integer, string, etc.)
 *
 * Return: True if value has been correctly printed (it means
 *         the value is an integer)
 *         Otherwise, returns False)
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
