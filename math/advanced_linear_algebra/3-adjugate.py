#!/usr/bin/env python3

def determinant(matrix):
    """input matrix. output determinant"""
    if matrix == [[]]:
        return 1
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


def minor(matrix):
    """base case: len(matrix) is 1 or 2"""
    if len(matrix) == 1:
        return [[1]]
    minor_mat = []
    for i in range(len(matrix)):  # loop through row
        row = []
        for j in range(len(matrix)):  # loop through column
            submatrix = [
                row[:j] + row[j + 1:]
                for row in (matrix[:i] + matrix[i + 1:])
            ]
            row.append(determinant(submatrix))
        minor_mat.append(row)
    return minor_mat


def cofactor(matrix):
    """Return cofactor"""
    minor_mat = minor(matrix)
    for i in range(len(minor_mat)):
        for j in range(len(minor_mat)):
            minor_mat[i][j] = (-1) ** (i + j) * minor_mat[i][j]
    return minor_mat


def matrix_transpose(matrix):
    """Input origignal matrix, output new transpose matrix"""
    new_matrix = []
    # get how many columns
    for col in range(len(matrix[0])):
        temp = []
        # get how many rows
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        new_matrix.append(temp)
    return new_matrix


def adjugate(matrix):
    if any(type(row) is not list for row in matrix) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    elif any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    adjugate_mat = matrix_transpose(cofactor(matrix))
    return adjugate_mat


# mat1 = [[5]]
# mat2 = [[1, 2], [3, 4]]
# mat3 = [[1, 1], [1, 1]]
# mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
# mat5 = []
# mat6 = [[1, 2, 3], [4, 5, 6]]

# print(adjugate(mat1))
# print(adjugate(mat2))
# print(adjugate(mat3))
# print(adjugate(mat4))
# try:
#     adjugate(mat5)
# except Exception as e:
#     print(e)
# try:
#     adjugate(mat6)
# except Exception as e:
#     print(e)
