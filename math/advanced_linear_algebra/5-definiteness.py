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
    if not np.array_equal(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)

    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"


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
