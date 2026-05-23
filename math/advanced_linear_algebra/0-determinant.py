#!/usr/bin/env python3

"""function that calculates the determinant of a matrix:"""


def determinant(matrix):
    """input matrix. output determinant"""
    if matrix == [[]]:
        return 1
    elif any(type(row) is not list for row in matrix) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    elif any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        total = 0
        for i in range(len(matrix)):  # first row element (3)
            det_matrix = []
            for row in range(len(matrix)):  # loop through row (3)
                temp = []
                for col in range(len(matrix[0])):  # loop through column(3)
                    if row == 0 or col == i:
                        pass
                    else:
                        temp.append(matrix[row][col])
                if temp:
                    det_matrix.append(temp)
            if i % 2 == 0:
                sign = 1
            else:
                sign = -1
            total = total + sign * determinant(det_matrix) * matrix[0][i]
    return total


# mat0 = [[]]
# mat1 = [[5]]
# mat2 = [[1, 2], [3, 4]]
# mat3 = [[1, 1], [1, 1]]
# mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
# mat5 = []
# mat6 = [[1, 2, 3], [4, 5, 6]]

# print(determinant(mat0))
# print(determinant(mat1))
# print(determinant(mat2))
# print(determinant(mat3))
# print(determinant(mat4))
# try:
#     determinant(mat5)
# except Exception as e:
#     print(e)
# try:
#     determinant(mat6)
# except Exception as e:
#     print(e)
