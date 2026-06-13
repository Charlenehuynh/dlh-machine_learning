#!/usr/bin/env python3
"""Create a class Exponential that represents an exponential distribution:"""


class Exponential:
    """lamtha = 1 / average of data"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.0):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            avg = 0
            for i in data:
                avg += i
            self.lambtha = 1 / (avg / len(data))

    def pdf(self, x):
        """lamtha * e ** (-lambtha * x)"""

        if x < 0:
            return 0
        pdf = self.lambtha * Exponential.e ** (-self.lambtha * x)
        return pdf

    def cdf(self, x):
        """CDF = 1 - e**(-lamtha * x)"""
        if x < 0:
            return 0
        cdf = 1 - Exponential.e ** (-self.lambtha * x)
        return cdf


# np.random.seed(0)
# data = np.random.exponential(0.5, 100).tolist()
# e1 = Exponential(data)
# print('F(1):', e1.cdf(1))

# e2 = Exponential(lambtha=2)
# print('F(1):', e2.cdf(1))
