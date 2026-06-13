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


# np.random.seed(0)
# data = np.random.normal(70, 10, 100).tolist()
# n1 = Normal(data)
# print("Mean:", n1.mean, ", Stddev:", n1.stddev)

# n2 = Normal(mean=70, stddev=10)
# print("Mean:", n2.mean, ", Stddev:", n2.stddev)
