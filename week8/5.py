import numpy as np
A = np.array([[1, np.nan, 3],[np.nan, np.nan, np.nan],[np.nan, 2, 3], [4, 5, np.nan]])


print(np.where(np.isnan(A), np.nanmean(A[np.argwhere(np.isnan(A))[0]]), A))




