import matplotlib.pyplot as plt
import numpy as np
y = input('Введи функцию y= ')
x = np.arange(-10,10.1,1)
with plt.xkcd():
    sp = plt.subplot()
    sp.spines['left'].set_position('center')
    sp.spines['bottom'].set_position('center')
    plt.plot(x, eval(y))
    plt.grid(color='red', lw=0.7)
    plt.show()