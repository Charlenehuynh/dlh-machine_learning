#!/usr/bin/env python3
"""Module that calculates a correlation matrix"""

import numpy as np


def correlation(C):
    """Calculate a correlation matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std = np.sqrt(np.diag(C))
    outer_std = np.outer(std, std)
    correlation_matrix = C / outer_std

    return correlation_matrix

# C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
# Co = correlation(C)
# print(C)
# print(Co)
