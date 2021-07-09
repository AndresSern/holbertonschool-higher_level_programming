""" #!/usr/bin/python3 """
import random
number = random.randint(-10000, 10000)
lastN = number % 10
if number < 0:
    lastN = (-number % 10) * -1
if lastN > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastN))
elif lastN == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastN))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastN))
