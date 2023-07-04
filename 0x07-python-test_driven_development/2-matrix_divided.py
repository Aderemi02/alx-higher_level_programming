#!/usr/bin/python3
"""a function that divides all element in a matrix"""


def matrix_divided(matrix, div):
    """this divides all element in the matrix
    the matrix is divided by the div parameter
    returns the matrix of the divided matrix
    """

    if (matrix == [] or not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or all((isinstance(num, int) or isinstance(num, float))
                   for num in [i for row in matrix for i in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda y: round(y / div, 2), row)) for row in matrix])
