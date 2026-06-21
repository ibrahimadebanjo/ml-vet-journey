import numpy as np
arr = np.array([(4,6,2),(7,9,2)])
#statistics
print(arr)
print(np.mean(arr, axis = 0))
print(np.mean(arr, axis = 1))
print(arr.sum())
print(arr.min())
print(arr.max(axis = 1 ))
print(np.var(arr))
print(np.std(arr, axis = 0))