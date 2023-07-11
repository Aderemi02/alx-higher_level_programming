#!/usr/bin/python3
"""
Create a function def pascal_triangle(n)
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    building the pascal triangle
    """

    if n <= 0:
        return []

    final_triangle = [[1]]
    while len(final_triangle) != n:
        temp_tri1 = final_triangle[-1]
        temp_tri2 = [1]
        for new in range(len(temp_tri1) - 1):
            temp_tri2.append(temp_tri1[new] + temp_tri1[new + 1])
        temp_tri2.append(1)
        final_triangle.append(temp_tri2)
    return final_triangle
