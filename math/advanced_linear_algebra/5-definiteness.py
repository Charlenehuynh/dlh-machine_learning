#!/usr/bin/env python3
"""calculate definiteness of a matrix"""

import numpy as np


def definiteness(matrix):
    """Return string:
    Positive definite
    """
    if type(matrix) is not np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")
    elif matrix.ndim != 2:
        return None
    elif matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None
    D1 = matrix[0][0]
    D2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    D3 = np.linalg.det(matrix)
    if D1 > 0 and D2 > 0 and D3 > 0:
        result = "Positive definite"
    elif D1 < 0 and D2 > 0:
        result = "Negative definite"
    elif any(d == 0 for d in [D1, D2, D3]) and all(d >= 0 for d in [D1, D2, D3]):
        result = "Positive semi-definite"
    elif any(d == 0 for d in [D1, D2, D3]) and (D1 <= 0 and D2 >= 0 and D3 <= 0):
        result = "Negative semi-definite"
    else:
        result = "Indefinite"
    print(D1, D2, D3)
    return result


# mat1 = np.array([[5, 1], [1, 1]])
# mat2 = np.array([[2, 4], [4, 8]])
# mat3 = np.array([[-1, 1], [1, -1]])
# mat4 = np.array([[-2, 4], [4, -9]])
# mat5 = np.array([[1, 2], [2, 1]])
# mat6 = np.array([])
# mat7 = np.array([[1, 2, 3], [4, 5, 6]])
# mat8 = [[1, 2], [1, 2]]

# print(definiteness(mat1))
# print(definiteness(mat2))
# print(definiteness(mat3))
# print(definiteness(mat4))
# print(definiteness(mat5))
# print(definiteness(mat6))
# print(definiteness(mat7))
# try:
#     definiteness(mat8)
# except Exception as e:
#     print(e)
