#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastN = number % 10
string = "Last digit of "
if number < 0:
    lastN = lastN * -1
if lastN > 5:
    print("{}{} is {} and is greater than 5".format(string, number, lastN))
elif lastN == 0:
    print("{}{} is {} and is 0".format(string, number, lastN))
elif lastN < 6 and lastN != 0:
    print("{}{} is {} and is less than 6 and not 0".format(string,
                                                               number,
                                                               lastN))
    Last digit of -4485 is -5 and is less than 6 and not 0
