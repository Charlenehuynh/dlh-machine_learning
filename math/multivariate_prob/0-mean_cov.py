#!/usr/bin/env python3
"""Module that calculates the mean and covariance of a data set"""

import numpy as np


def mean_cov(X):
    """Calculates the mean and covariance of a data set"""
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n = X.shape[0]

    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0, keepdims=True)
    deviation = X - mean
    cov = np.matmul(deviation.T, deviation) / (n - 1)

    return mean, cov


# np.random.seed(0)
# X = np.random.multivariate_normal([12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000)
# mean, cov = mean_cov(X)
# print(mean)
# print(cov)
