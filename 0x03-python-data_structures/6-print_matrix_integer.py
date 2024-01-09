#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for smax in matrix:
        for idx in range(len(smax):
            if idx != len(smax) - 1:
                print("{:d} ".format(smax[idx]), end="")
            else:
                print("{:d}".format(smax[idx]), end="")
        print()
