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

    def pdf(self, x):
        "Calculates the PDF at a data point"
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        deviation = x - self.mean
        exponent = -0.5 * np.matmul(np.matmul(deviation.T, inv), deviation)

        denominator = np.sqrt(((2 * np.pi) ** d) * det)

        pdf_value = (1 / denominator) * np.exp(exponent[0][0])

        return pdf_value


np.random.seed(0)
data = np.random.multivariate_normal(
    [12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 10000
).T
mn = MultiNormal(data)
x = np.random.multivariate_normal(
    [12, 30, 10], [[36, -30, 15], [-30, 100, -20], [15, -20, 25]], 1
).T
print(x)
print(mn.pdf(x))
