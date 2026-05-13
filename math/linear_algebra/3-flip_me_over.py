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


# mat1 = [[1, 2], [3, 4]]
# print(mat1)
# print(matrix_transpose(mat1))
# mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
# print(mat2)
# print(matrix_transpose(mat2))
