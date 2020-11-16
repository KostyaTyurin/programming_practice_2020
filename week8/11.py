import numpy as np
n = int(input())
matrix = np.zeros((n,n))

for i in range(n):
    for k in range(n):
        if i % 2 == 0 and k % 2 == 1:
            matrix[i][k] = 1
        if i % 2 == 1 and k % 2 == 0:
            matrix[i][k] = 1

print(matrix)
