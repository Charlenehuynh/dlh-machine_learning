#!/usr/bin/env python3
"""Add 2 arrays"""


def add_arrays(arr1, arr2):
    """Add 2 arrays and return a new list of int/float"""
    new_list = []
    if len(arr1) != len(arr2):
        return None
    for i in range(len(arr1)):
        new_list.append(arr1[i] + arr2[i])
    return new_list


# arr1 = [1, 2, 3, 4]
# arr2 = [5, 6, 7, 8]
# print(add_arrays(arr1, arr2))
