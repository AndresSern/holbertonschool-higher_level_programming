#!/usr/bin/python3
def print_last_digit(number):
    lastNumber = number % 10
    if number < 0:
        lastNumber = (-number % 10)
    print("{:d}".format(lastNumber), end='')
    return lastNumber
