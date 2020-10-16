import matplotlib.pyplot as plt
import numpy as np

def func(x):

        if -10 <= x < -5:
            return 2 * abs(x)
        if -5 <= x <= 5:
            return x ** 2
        if 5 < x <= 10:
            return 2 * x
poolx = []
pooly = []
for x in range(-10, 11, 1):
    poolx.append(x)
    y = func(x)
    pooly.append(y)
    print('y (',x,') = ', y)

plt.figure(10)
plt.grid(True)
plt.plot(poolx, pooly, 'ro')
plt.ylabel('f(x)', fontsize = 15)
plt.xlabel('x', fontsize = 15)
plt.show()

