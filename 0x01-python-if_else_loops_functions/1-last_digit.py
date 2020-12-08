#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastN = number % 10
string = "Last digit of "
if lastN > 5:
    print("{}{:d} is {:d} and is greater than 5".format(string, number, lastN))
elif lastN == 0:
    print("{}{:d} is {:d} and is 0".format(string, number, lastN))
else:
    print("{}{:d} is {:d} and is less than 6 and not 0".format(string,
                                                               number,
                                                               lastN))
