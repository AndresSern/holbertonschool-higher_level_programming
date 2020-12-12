#!/usr/bin/python3
def fizzbuzz():
    count = 1
    while(count < 100):

        if count % 5 == 0 and count % 3 == 0:
            print("FizzBuzz ", end='')
        elif count % 3 == 0:
            print("Fizz ", end='')
        elif count % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(count), end='')
        count += 1
    print("Buzz ", end='')
