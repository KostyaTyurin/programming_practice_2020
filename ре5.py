import matplotlib.pyplot as plt
import numpy as nmp

x = list(map(int, input().split()))
y = list(map(float, input().split()))
n = len(x)
for i in range(n):
    plt.plot(x[i], y[i], 'ro')
plt.errorbar(x, y, xerr=0.1, yerr=0.2)
p, v = nmp.polyfit(x,y,  deg=2, cov=True)
p_f= nmp.poly1d(p)
print(p_f)
plt.grid()
plt.plot(x, p_f(x))
plt.grid()
p, v = nmp.polyfit(x,y, deg=6, cov=True)
s_f=nmp.poly1d(p)
print(s_f)
plt.plot(x, s_f(x))
plt.grid()
plt.show()