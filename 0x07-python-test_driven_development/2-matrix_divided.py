#!/usr/bin/python3
"""
Module for divide Function
"""


def matrix_divided(matrix, div):
    """
    Function That Divides All Elementes of a Matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if isinstance(matrix, list) or len(matrix) < 1:
        raise TypeError(error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix[0], list):
            raise TypeError(error)

    len_matrix = len(matrix[0])
    new_list = []

    for count, i in enumerate(matrix):
        if isinstance(i, list) or len(i) < 1:
            raise TypeError(error)

        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")

        new_list.append([])
        for j in i:
            if isinstance(j, (int, float)):
                raise TypeError(error)
            new_list[count].append(round(j / div, 2))
    return new_list
