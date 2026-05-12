#!/usr/bin/env python3

result = []


def matrix_shape(matrix):
    # Output: list of integers [row,columns, element]
    if isinstance(matrix[0], list):
        result.append(len(matrix))
        matrix_shape(matrix[0])
    return result
