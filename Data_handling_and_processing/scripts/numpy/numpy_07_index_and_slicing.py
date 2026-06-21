import numpy as np
arr = np.array([(1,2,3),(5,8,20),(9,5,0),(1,8,5),(7,5,6)])
print(arr[4])
print(arr)
print(arr[0,2])
arr[2] = 9
print(arr)
#slicing
print("slicing")
print(arr[0:3])
print(arr[0:2, 2])
print(arr[:2])
print(arr[:,1])
