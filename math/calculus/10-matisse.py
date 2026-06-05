#!/usr/bin/env python3
"""that calculates the derivative of a polynomial:"""


def poly_derivative(poly):
    """derivative of polynomial"""
    if not isinstance(poly, list) or not poly:
        return None
    if len(poly) == 1:
        return [0]
    ls = []
    for i in range(1, len(poly)):
        ls.append(poly[i] * i)
    while len(ls) > 1 and ls[-1] == 0:
        ls.pop()
    return ls


# poly = ["not list", 3, 0, 1]
# print(poly_derivative(poly))
