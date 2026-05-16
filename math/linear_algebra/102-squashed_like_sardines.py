#!/usr/bin/env python3
"""Concat matrix along axis"""


def cat_matrices(mat1, mat2, axis=0):
    """Input mat1,mat2 output new matrix"""
    result = []
    if axis == 0:
        if isinstance(mat1[0], list) and len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    else:
        if len(mat1) != len(mat2):
            return None
        for row1, row2 in zip(mat1, mat2):
            temp = cat_matrices(row1, row2, axis - 1)
            if temp is None:
                return None
            result.append(temp)
    return result


# mat3 = [[[[1, 2, 3, 4], [5, 6, 7, 8]],
#          [[9, 10, 11, 12], [13, 14 ,15, 16]],
#          [[17, 18, 19, 20], [21, 22, 23, 24]]],
#         [[[25, 26, 27, 28], [29, 30, 31, 32]],
#          [[33, 34, 35, 36], [37, 38, 39, 40]],
#          [[41, 42, 43, 44], [45, 46, 47, 48]]]]
# mat4 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
#          [[19, 110, 111, 112], [113, 114 ,115, 116]],
#          [[117, 118, 119, 120], [121, 122, 123, 124]]],
#         [[[125, 126, 127, 128], [129, 130, 131, 132]],
#          [[133, 134, 135, 136], [137, 138, 139, 140]],
#          [[141, 142, 143, 144], [145, 146, 147, 148]]]]
# mat5 = [[[[11, 12, 13, 14], [15, 16, 17, 18]],
#          [[117, 118, 119, 120], [121, 122, 123, 124]]],
#         [[[125, 126, 127, 128], [129, 130, 131, 132]],
#          [[141, 142, 143, 144], [145, 146, 147, 148]]]]

# m = cat_matrices(mat3, mat4, axis=3)
# print(m)
