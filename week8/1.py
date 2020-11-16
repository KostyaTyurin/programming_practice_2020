
import numpy as np
import matplotlib.pyplot as plt
import random
import time
np_values = np.random.randint(1000, size=(100, 2))
values_std = [[random.randint(0, 1000), random.randint(0, 1000)] for i in range(100)]
np_time = []
standard_time = []


def f(x, y):
    return 2 * x ** 2 + 4 * y


def numpy_f(arr):
    return 2 * arr.T[0] ** 2 + 4 * arr.T[1]


def standard_f(arr):
    return [f(x, y) for (x, y) in arr]


for i in range(1000):
    start = time.time()

    numpy_f(np_values)
    end = time.time()
    np_time.append(end - start)

for i in range(1000):
    start = time.time()
    standard_f(np_values)
    end = time.time()
    standard_time.append(end - start)

plt.plot(np_time, color="red")
plt.plot(standard_time, color="blue")
plt.show()
