import numpy as np
m = float(input())
def min(m):
    i = np.random.randint(1, 20)
    j = np.random.randint(1, 20)
    A = np.random.random((i, j))
    A *= 100
    M  = np.full((i,j), m)
    razn = abs(A - M)
    index_min = np.argmin(razn)
    return print(A.flat[index_min])

min(m)

