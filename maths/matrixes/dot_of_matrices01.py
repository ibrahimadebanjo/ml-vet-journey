import numpy as np
a = np.random.randint(5, size = (3,4))
b = np.random.randint(5, size = (4,2))
print("matrix A")
print(a)
print("matrix B")
print(b)
product = np.dot(a,b) #or use np.multiply() function but for this function to work, both matrices must have same shape
print("Dot of matrux A and B") 
print(product)