#!/usr/bin/env python3
"""Multiply matrix"""


def mat_mul(mat1, mat2):
    """Multiply matrix"""
    # determine if matrix is valid (1st matrix column
    # is name is 2nd matrix row)

    if len(mat1[0]) != len(mat2):
        return None
    result = []
    # loop row of matrix 1
    for row in range(len(mat1)):
        temp = []
        # loop column of matrix 2
        for col in range(len(mat2[0])):
            # matrix loop:
            sum = 0
            for index in range(len(mat1[0])):  # 0 - 2
                sum += mat1[row][index] * mat2[index][col]
            temp.append(sum)
        result.append(temp)
    return result


# mat1 = [[1, 2], [3, 4], [5, 6]]  # 3  x 2
# mat2 = [[1, 2, 3, 4], [5, 6, 7, 8]]  # 2 x 4
# # final matrix:
# """[1* 1 + 2*5]
#         # 1 * 1 + 2 * 5
#         mat1[0][0] * mat2[0][0] + mat1[0,1] * mat2[1,0]
#         mat1[0,1] * mat2[1,0] + mat1[1,1] * mat2[1,1]
#         mat1[1,0] * mat2[2,0] + mat1[2,1] * mat2[2,1]
#         mat1[0,1] * mat2[+1,0] + mat1[+1,1] * mat2[]
# """

# # final matrix: 3 x 4
# print(mat_mul(mat1, mat2))
