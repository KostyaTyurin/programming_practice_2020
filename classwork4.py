import matplotlib.pyplot as plt
import numpy as np
y = input()
x = np.arange(-10,10.01,0.01)
with plt.xkcd():
    plt.plot(eval(y))
    plt.show()