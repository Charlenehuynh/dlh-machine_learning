#!/usr/bin/env python3

def poly_derivative(poly):
    if not isinstance(poly, list):
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


# poly = [5, 3, 0, 1]
# print(poly_derivative(poly))
