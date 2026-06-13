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

    def cdf(self, x):
        """F(x) = (1/2) * (1 + erf(z / √2))
        erf(x) ≈ 1 - (a1t + a2t² + a3t³) * e^(-x²)
        where t = 1 / (1 + 0.47047x)"""
        z = Normal.z_score(self, x)
        x_abs = abs(z / 2**0.5)
        # calculate erf using more precise coefficients:
        t = 1 / (1 + 0.3275911 * x_abs)
        erf = 1 - (
            0.254829592 * t
            - 0.284496736 * t**2
            + 1.421413741 * t**3
            - 1.453152027 * t**4
            + 1.061405429 * t**5
        ) * Normal.e ** (-(x_abs**2))
        if z < 0:
            erf = -erf
        return 0.5 * (1 + erf)


# np.random.seed(0)
# data = np.random.normal(70, 10, 100).tolist()
# n1 = Normal(data)
# print("PHI(90):", n1.cdf(90))

# n2 = Normal(mean=70, stddev=10)
# print("PHI(90):", n2.cdf(90))
