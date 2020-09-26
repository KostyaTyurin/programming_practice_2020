import numpy as np
x = list(map(int, input('Введите числа ').split()))
n = len(x)
for i in range(n):
    y = (np.log(1/np.e**np.sin(x[i])+1)-(np.log((5/4) + 1/x[i]**15 )))/np.log(1+x[i]**2)
    print('y(',x[i],')=',y)
