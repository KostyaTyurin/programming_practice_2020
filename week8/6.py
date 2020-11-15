import numpy as np

a = np.array([[1,2, 3], [0.1, 0.5, 6], [6,78,-100]])
def norm(a):
    while len(a[abs(a) > 1]) > 0:
        a[abs(a) > 1] /= 10
    return print(a)
norm(a)
