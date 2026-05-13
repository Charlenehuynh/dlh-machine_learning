#!/usr/bin/env python3
"""Add 2 matrices element wise"""


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result = []
    for row in range(len(mat1)):
        temp = []
        for element in range(len(mat1[0])):
            temp.append(mat1[row][element] + mat2[row][element])
        result.append(temp)
    return result


# mat1 = [[1, 2], [3, 4]]
# mat2 = [[5, 6], [7, 8]]
# print(add_matrices2D(mat1, mat2))
