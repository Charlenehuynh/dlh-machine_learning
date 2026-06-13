#!/usr/bin/env python3
"""Create a class Normal that represents a normal distribution"""


class Normal:
    """mean == average ; stddev = square root (sum(i - mean)^2 / n)"""

    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        mean = float(mean)
        stddev = float(stddev)
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = mean
            self.stddev = stddev
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # calculate mean : average
            sum = 0
            for i in data:
                sum += i
            self.mean = sum / len(data)
            # calculate standard deviation: square root (sum(i - mean)^2 / n)
            result = 0
            for i in data:
                result += (i - self.mean) ** 2
            self.stddev = (result / len(data)) ** 0.5

    def z_score(self, x):
        """z = (x - mean) / standard deviation"""
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """x = (z - mean) / standard deviation"""
        x = (z * self.stddev) + self.mean
        return x

    def pdf(self, x):
        """f(x) = (1 / (stddev * √(2π))) * e^(-0.5 * z²)"""
        z = Normal.z_score(self, x)
        pdf = (1 / (self.stddev * (2 * Normal.pi) ** 0.5)) * Normal.e ** (-0.5 * z**2)
        return pdf

    def erf(self, x):
        """calculate erf"""
        k = 2 / (Normal.pi**0.5)
        t3 = (x**3) / 3
        t5 = (x**5) / 10
        t7 = (x**7) / 42
        t9 = (x**9) / 216
        return k * (x - t3 + t5 - t7 + t9)

    def cdf(self, x):
        """calculate"""
        z = self.z_score(x)
        cdf = 0.5 * (1 + self.erf(z / (2**0.5)))
        return cdf


# import numpy as np
# np.random.seed(0)
# data = np.random.normal(70, 10, 100).tolist()
# n1 = Normal(data)
# print("PHI(90):", n1.cdf(90))

# n2 = Normal(mean=70, stddev=10)
# print("PHI(90):", n2.cdf(90))
