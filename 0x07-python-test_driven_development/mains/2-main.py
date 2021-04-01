#!/usr/bin/python3
""" Doc """

matrix_divided = __import__('2-matrix_divided').matrix_divided

#try:
matrix = [[1, 0, 3], [4, 5.6, 6]]
print(matrix_divided(matrix, 0))
print(matrix)
#except Exception as e:
    #print(e)

#try:
matrix = [[3, "9"], [15, 3]]
print(matrix_divided(matrix, 3))
print(matrix)
#except Exception as e:
#    print(e)
