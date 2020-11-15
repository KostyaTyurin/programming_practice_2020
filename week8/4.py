import numpy as np
import random
i = random.randint(10,100)
matrix = np.random.randint(-100, 100, size=(i, i))
max = np.max(matrix)
min = np.min(matrix)
sum = np.sum(matrix)

new_matrix1 = matrix / max
last_matrix = matrix
matrix2 = np.array(matrix, dtype = 'float64')
print(matrix2)

for j in range(i):
    a = np.mean(matrix2[j])
    for k in range(i):
        matrix2[j][k] -= a
last_matrix[last_matrix == max] = -1

print(matrix, max, min, sum, new_matrix1, last_matrix )

print(matrix2)

