#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastN = number % 10
if lastN > 5:
    print("Last digit of {:d} is {:d} and is greater thn 5".format(number,
                                                                    lastN))
elif lastN == 0:
    print("Last digit of {:d} is {:d} and is ".format(number, lastN))
else:
    print("Last digit of {:d} is {:d} is less than 6 and not ".format(
                                                                    number,
                                                                    lastN))
