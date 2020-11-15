import numpy as np
a = np.arange(1, 10)
b = np.arange(1, 7)


c = a[~np.in1d(a, b)]
k = a[np.in1d(a, b, invert =True)]
m = a[np.isin(a,b, invert=True)]
print(a, b, c, k, m)
