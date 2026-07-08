#!/usr/bin/env python3
import string
import numpy as np
import pandas as pd


def from_numpy(array):
    size = array.shape
    column = list(string.ascii_uppercase[: size[1]])
    df = pd.DataFrame(array, columns=column)
    return df


# np.random.seed(0)
# A = np.random.randn(5, 8)
# print(from_numpy(A))
# B = np.random.randn(9, 3)
# print(from_numpy(B))
