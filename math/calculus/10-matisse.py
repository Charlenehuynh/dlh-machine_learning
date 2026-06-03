#!/usr/bin/env python3
""" that calculates the derivative of a polynomial: """


def poly_derivative(poly):
    """ derivative of polynomial"""
    if not (isinstance(poly, list) & all(isinstance(i, int) for i in poly)):
        return None
    if len(poly) == 1:
        return [0]
    ls = []
    for i in range(1, len(poly)):
        if poly[i] == 0:
            ls.append(0)
        else:
            ls.append(poly[i] * i)
    if all(num == 0 for num in ls):
        return [0]
    return ls


# poly = ["not list", 3, 0, 1]
# print(poly_derivative(poly))
