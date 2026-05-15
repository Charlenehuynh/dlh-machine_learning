#!/usr/bin/env python3
"""concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Args: matrix
    Output new concatenated matrix
    """

    if axis == 0:
        new = []
        if len(mat1[0]) != len(mat2[0]):
            return None
        for row in mat1:
            new.append(row[:])
        for row in mat2:
            new.append(row[:])
        return new
    else:
        if len(mat1) != len(mat2):
            return None
        new = []
        for i in range(len(mat1)):
            new.append(mat1[i] + mat2[i])
        return new

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
