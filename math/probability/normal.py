#!/usr/bin/env python3
"""Create a class Normal that represents a normal distribution"""


class Normal:
    """mean == average ; stddev = square root (sum(i - mean)^2 / n)"""

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


# np.random.seed(0)
# data = np.random.normal(70, 10, 100).tolist()
# n1 = Normal(data)
# print('Z(90):', n1.z_score(90))
# print('X(2):', n1.x_value(2))

# n2 = Normal(mean=70, stddev=10)
# print()
# print('Z(90):', n2.z_score(90))
# print('X(2):', n2.x_value(2))
