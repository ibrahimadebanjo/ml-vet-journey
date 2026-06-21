import numpy as np
arr1 = np.array([(1,2,3),(4,5,6)])
arr2 = np.array([(6,7,8),(8,9,6)])
#concatenate
new_arr = np.concatenate((arr1, arr2), axis= 0)
print(new_arr)
new_arr = np.concatenate((arr1, arr2), axis= 1)
print(new_arr)
#split
print(np.split(new_arr, 2))
print(np.hsplit(new_arr, 3))

