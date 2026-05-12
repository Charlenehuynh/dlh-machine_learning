#!/usr/bin/env python3
"""Recursion"""


def matrix_shape(matrix):
    # Output: list of integers [row,columns, element]
    if isinstance(matrix[0], list):
        return [len(matrix)] + matrix_shape(matrix[0])
    else:
        return [len(matrix)]


# mat1 = [[1, 2], [3, 4]]
# print(matrix_shape(mat1))
# mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
#         [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
# print(matrix_shape(mat2))
