#!/usr/bin/env python3
"""Slice matrix along specific axess"""

import numpy as np


def np_slice(matrix, axes={}):
    """Output new matrix"""
    result = matrix
    for k, value in axes.items():
        # if axes.key == 0: ## horizontal
        if k == 0:
            result = result[value[0]: value[1], :]
        if k == 1:
            result = result[ : , value[0] : value[1]]
        else:
    return result
    return result
    return result


    # else: #slice vertical


mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_slice(mat1, axes={0: (0, 1)}))
