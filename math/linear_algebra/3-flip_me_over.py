#!/usr/bin/env python3


def matrix_transpose(matrix):
    new_matrix = []
    # get how many columns
    for col in range(len(matrix[0])):
        temp = []
        # get how many rows
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        new_matrix.append(temp)
    return new_matrix


mat1 = [[1, 2, 3], [4, 5, 6]]
print(matrix_transpose(mat1))
