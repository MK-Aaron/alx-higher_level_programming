#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix

    new_matrix = [square_array(r.copy()) for r in matrix]
    return new_matrix


def square_array(arr):
    return [i**2 for i in arr]
