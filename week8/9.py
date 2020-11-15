import numpy as np
rows = int(input())
colums = int(input())
num = int(input())

start = int(input())
end = int(input())
def matrix(rows, colums, num, start, end):
    A = np.full((rows,colums), num)
    A[0][0] = start
    A[rows-1][colums - 1] = end
    return print(A)
matrix(rows, colums, num, start, end)
