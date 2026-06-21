import numpy as np
arr = np.array([(1,2,3), (2,8,6)])
print(arr)
values = (8,9,19)
#append
new_arr  = np.append(arr, values)
print(new_arr)
#imsert
inserted = np.insert(arr, 0, values)
print(inserted)
#delete 
deleted = np.delete(arr, 0,  axis = 0)
print(deleted)
deleted = np.delete(arr, 1, axis = 1)
print(deleted)