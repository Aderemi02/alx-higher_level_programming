#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = matrix.copy()
    for i in range (len(result)):
        result[i] = list(map(lambda new: new * new, result[i]))
        return result

