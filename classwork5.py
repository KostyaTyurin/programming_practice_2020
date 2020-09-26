import numpy as np
import matplotlib.pyplot as plt
x = list(map(int, input().split()))
y = list(map(float, input().split()))
a = np.arange(-10, 10, 0.01)


sp = plt.subplot(112)
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
plt.plot(a, p_f(a))
print(p_f)

sp = plt.subplot(112)
p, v = np.polyfit(x, y, deg=2, cov=True)
g_f = np.poly1d(p)
plt.plot(a, g_f(a))
print(g_f)
plt.show()


