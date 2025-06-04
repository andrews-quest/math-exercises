import numpy as np
import matplotlib.pyplot as plt
import math

A = [[10, -1, 0, 2, 3, 1],
     [-1, 17, 2, -3, 1, 4],
     [0, 2, 23, 7, 1, 5],
     [2, -3, 7, 19, 1, 1],
     [3, 1, 1, 1, 9, -2],
     [1, 4, 5, 1, -2, 14]]
A_ = None
L = [[0 for elem in row] for row in A]


def calc_A_(A):
    A_ = [[0 for elem in row[:-1]] for row in A[:-1]]
    for row_num in range(0, len(A)-1):
        for elem_num in range(0, len(A[row_num])-1):
            A_[row_num][elem_num] = round(A[row_num+1][elem_num+1] - (A[row_num+1][0] * A[0][elem_num+1]) / A[0][0], 2)
    return A_

def alforithm(A, iter):

    # diagonal element
    L[iter][iter] = round(math.sqrt(A[0][0]), 2)

    # column elements
    for row_num in range(1, len(A)):
        L[iter + row_num][iter] = round(A[row_num][0] / math.sqrt(A[0][0]), 2)
    return L


L = alforithm(A, 0)
for iter in range(0, len(A)-1):
    A_ = calc_A_(A)
    L = alforithm(A_, iter+1)
    for elem in A_:
        print(elem)

    print("\nL currently is:")
    for elem in L:
        print(elem)
    print(" ")
    A = A_

print(f"\nL is:\n")
for row in L:
    print(row)

