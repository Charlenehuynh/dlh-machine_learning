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

    def pmf(self, k):
        """P(X = k) = C(n, k) * p^k * (1-p)^(n-k)"""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        n_fact = 1
        for i in range(1, self.n + 1):
            n_fact *= i
        k_fact = 1
        for i in range(1, k + 1):
            k_fact *= i
        nk_fact = 1
        for i in range(1, (self.n - k) + 1):
            nk_fact *= i
        binomial_coeff = n_fact / (k_fact * nk_fact)
        return binomial_coeff * (self.p**k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """ CDF """
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)
        return cdf_value


# np.random.seed(0)
# data = np.random.binomial(50, 0.6, 100).tolist()
# b1 = Binomial(data)
# print('F(30):', b1.cdf(30))

# b2 = Binomial(n=50, p=0.6)
# print('F(30):', b2.cdf(30))
