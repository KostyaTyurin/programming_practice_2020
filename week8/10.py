import numpy as np
A = np.array([[1, 2, 3, 4], [2, -6, 78, 45], [23, 10, 100, 67], [0, 0, 0, 0]])
s = int(input()) - 1


def sort(A, s):
    shape = np.shape(A)

    M = shape[0]
    N = shape[1]
    k = M - 1
    while k > 0:
        ind = 0
        for j in range(k+1):
            if A[j][s] > A[ind][s]:
                ind = j
        for i in range(N):
            m = A[ind][i]
            A[ind][i] = A[k][i]
            A[k][i] = m
        k -= 1
    return print(A)


sort(A, s)
