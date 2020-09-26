import numpy as np
import matplotlib.pyplot as plt
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = np.arange(-10, 10, 0.01)
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
plt.plot(a, p_f(list(a)))
print(p_f)
plt.show()
