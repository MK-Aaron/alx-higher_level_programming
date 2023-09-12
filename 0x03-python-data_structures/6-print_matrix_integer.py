#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        row = len(matrix)
        if row > 0 and len(matrix[0]) > 0:
            for i in range(row):
                column = len(matrix[i]) - 1
                for j in range(column):
                    print("{:d}".format(matrix[i][j]), end=" ")
                print("{:d}".format(matrix[i][column]))
        else:
            print()
