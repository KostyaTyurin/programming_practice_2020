import matplotlib.pyplot as plt
import numpy as np
x= np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2-x-6, x, 0*x, )
plt.grid(color='blue',linewidth=0.1)
plt.show()