#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for i in matrix:
        matrix_square.append(list(map(lambda x: x * x, i)))
    return (matrix_square)
