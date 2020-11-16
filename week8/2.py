import numpy as np
a = np.arange(2,76)
b = a[a % 2 == 1]
a[a % 2 == 1] = -1
print(b)
print(a)
