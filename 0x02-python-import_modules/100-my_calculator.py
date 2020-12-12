#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    numb1 = int(argv[1])
    numb2 = int(argv[3])

    if argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] is "+":
        print("{} + {} = {}".format(numb1, numb2, add(numb1, numb2)))
    elif argv[2] is "-":
        print("{} - {} = {}".format(numb1, numb2, sub(numb1, numb2)))
    elif argv[2] is "*":
        print("{} * {} = {}".format(numb1, numb2, mul(numb1, numb2)))
    elif argv[2] is "/":
        print("{} / {} = {}".format(numb1, numb2, div(numb1, numb2)))
