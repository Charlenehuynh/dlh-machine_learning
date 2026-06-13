#!/usr/bin/env python3
"""Create a class Poisson that represents a poisson distribution:"""


class Poisson:
    """Poisson"""

    def __init__(self, data=None, lambtha=1.0):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """(lambtha^k *e ^(-lamtha)) / k!"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        sum = 1
        for i in range(1, k + 1):
            sum *= i
        pmf_value = (self.lambtha**k * e ** (-self.lambtha)) / sum
        return pmf_value

    def cdf(self, k):
        """PM(0) + PM(1)"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        total = 0
        for i in range(k + 1):
            pmf_value = Poisson.pmf(self, i)
            total += pmf_value
        return total


# np.random.seed(0)
# data = np.random.poisson(5.0, 100).tolist()
# p1 = Poisson(data)
# print("F(9):", p1.cdf(9))

# p2 = Poisson(lambtha=5)
# print("F(9):", p2.cdf(9))
