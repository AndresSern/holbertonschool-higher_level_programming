#!/usr/bin/python3
"""
Module for divide Function
"""


def matrix_divided(matrix, div):
    """
    Function That Divides All Elementes of a Matrix
    """
    if div is 0:
        raise TypeError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    len_matrix = len(matrix[0])
    new_list = []
    for count, i in enumerate(matrix):
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if len(i) != len_matrix:
            raise TypeError("Each row of the matrix must have the same size")
        new_list.append([])
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_list[count].append(round(j / div, 2))
    return new_list
