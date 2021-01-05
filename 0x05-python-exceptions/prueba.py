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
b = "2"

try:
    print("{:d}".format(b))
except ZeroDivisionError:
    print("hola")
