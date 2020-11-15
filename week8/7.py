import numpy as np
a = np.arange(12).reshape(3, 4)
np.save('hw', a)
print(a)
