#!/usr/bin/env python3
"""that calculates the integral of a polynomial:"""


def poly_integral(poly, C=0):
    """integral of polynomial"""
    if not isinstance(poly, list) or not isinstance(C, int):
        return None
    if not all(isinstance(i, (int, float)) for i in poly):
        return None
    ls = [C]
    for i in range(0, len(poly)):
        # ls.append(poly[i] / (i + 1))
        temp = poly[i] / (i + 1)
        ls.append(int(temp) if temp % 1 else temp)
    while len(ls) > 1 and ls[-1] == 0:
        ls.pop()
    return ls


# poly = [5, 3, 0, 1]
# print(poly_integral(poly))
