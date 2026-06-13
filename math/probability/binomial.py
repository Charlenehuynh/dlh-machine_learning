#!/usr/bin/env python3
"""Create a class Binomial that represents a binomial distribution"""


class Binomial:
    """class Binomial"""

    def __init__(self, data=None, n=1, p=0.5):
        """n = mean / p and p = 1 - (variance / mean)"""
        n = int(n)
        p = float(p)
        if data is None:
            self.n = n
            self.p = p
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            sum = 0
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # calculate mean
            for i in data:
                sum += i
            mean = sum / len(data)
            # variance (data_point - mean)² / len
            result = 0
            for i in data:
                result += (i - mean) ** 2
            variance = result / len(data)
            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n


# np.random.seed(0)
# data = np.random.binomial(50, 0.6, 100).tolist()
# b1 = Binomial(data)
# print('n:', b1.n, "p:", b1.p)

# b2 = Binomial(n=50, p=0.6)
# print('n:', b2.n, "p:", b2.p)
