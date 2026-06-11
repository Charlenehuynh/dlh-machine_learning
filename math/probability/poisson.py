#!/usr/bin/env python3

class Poisson:
    def __init__(self, data=None, lambtha=1.):
        self.data = data
        self.lambtha = float(lambtha)
        if data is None:
            return None
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if self.lambtha < 0 or lambtha == 0:
            raise ValueError("lambtha must be a positive value")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        sum = 0
        for i in data:
            sum = sum + i
            print(sum)
        self.lambtha = sum / len(data)

    def pmf(self, k):
        if not isinstance(k, int):
            k = int(k)
        
# import numpy as np

# np.random.seed(0)
# data = np.random.poisson(5., 100).tolist()
# p1 = Poisson(data)
# print('Lambtha:', p1.lambtha)

# p2 = Poisson(lambtha=5)
# print('Lambtha:', p2.lambtha)
