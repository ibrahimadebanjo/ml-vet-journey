import numpy as np
#transpose of matrix 
rand_matrix = np.random.randint(20, size = (4,6))
print(rand_matrix)
#find transpose of a matrix
print("transpose of above matrix appears bellow")
transpose_matrix = np.transpose(rand_matrix)
print(transpose_matrix)