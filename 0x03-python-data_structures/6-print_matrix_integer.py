#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner in matrix:
        ln = len(inner)
        if ln == 0:
            print("")
        else:
            for a in range(ln):
                if a < ln - 1:
                    print("{:d}".format(inner[a]), end=" ")
                else:
                    print("{:d}".format(inner[a]))
