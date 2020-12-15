#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for j in i:
            print("{}".format(j), end="")
            if count != (len(matrix) - 1):
                print(" ", end="")
            count += 1
        print("")
