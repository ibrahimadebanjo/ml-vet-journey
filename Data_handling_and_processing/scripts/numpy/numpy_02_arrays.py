import numpy as np
#1D array
arr = np.array([1,2,3])
#2D array
arr = np.array([(1,2,3), (4,5,7)])
#zeros
arr = np.zeros(4)
#ones
arr = np.ones((3,4)) #3x4 matrix
#eye
arr = np.eye(4)
#linspace
arr = np.linspace(0,100,6)
#Arange
arr = np.arange(0,10,3)
#full
arr = np.full((2,3), 3)
#Rand
arr = np.random.rand(7,9)
arr = np.random.rand(3,2) * 10
#Randint
arr = np.random.randint(5, size = (3,4))
print(arr)