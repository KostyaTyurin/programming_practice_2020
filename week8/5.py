import numpy as np
A = np.array([[1, np.nan, 3],[np.nan, np.nan, np.nan],[np.nan, 2, 3], [4, 5, np.nan]])



def ma(A):
   shape = np.array(np.shape(A))
   for i in range(shape[0]):
       if len(A[i][np.isfinite(A[i])]) == 0:
            A[i] = np.nan_to_num(A[i])
       else:
           A[i][np.isnan(A[i])] = np.nanmean(A[i])
   return print(A)
ma(A)



