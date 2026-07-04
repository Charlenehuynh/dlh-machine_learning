#!/usr/bin/env python3
"""Module that defines the multinormal class"""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """Class constructor"""
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        mean = np.mean(data, axis=1, keepdims=True)
        deviation = data - mean
        cov = np.matmul(deviation, deviation.T) / (n - 1)

        self.mean = mean
        self.cov = cov


# np.random.seed(0)
# data = np.random.multivariate_normal(
#     [12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000
# ).T
# mn = MultiNormal(data)
# print(mn.mean)
# print(mn.cov)
