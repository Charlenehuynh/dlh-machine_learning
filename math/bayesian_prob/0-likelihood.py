#!/usr/bin/env python3
"""calculates the likelihood of obtaining this data"""

import numpy as np


def likelihood(x, n, P):
    """hypothetical probabilities"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that " "is " "greater than or equal to 0"
        )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    factorial = np.math.factorial
    n_choose_x = factorial(n) / (factorial(x) * factorial(n - x))

    likelihoods = n_choose_x * (P**x) * ((1 - P) ** (n - x))

    return likelihoods


# P = np.linspace(0, 1, 11) # [0.0, 0.1, 0.2, 
# 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# print(likelihood(26, 130, P))
