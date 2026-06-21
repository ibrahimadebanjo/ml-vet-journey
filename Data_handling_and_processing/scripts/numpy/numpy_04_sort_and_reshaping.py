import numpy as np
arr = np.array([(1,2,3),(6,7,8)])
print(arr)
#copying
np.copy(arr)
#transpose
print(arr.T)
#sorting
print(arr.sort())
#reshaping
print(arr.reshape(2,3))
#resizing
resize = arr.resize((4,7))
print(resize)
