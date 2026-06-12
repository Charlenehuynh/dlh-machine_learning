#!/usr/bin/env python3
"""Create a class Poisson that represents a poisson distribution"""


class Poisson:
    """class Poisson"""

    def __init__(self, data=None, lambtha=1.0):
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
        self.lambtha = sum / len(data)
