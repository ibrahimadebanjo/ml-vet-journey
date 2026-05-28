import numpy as np
#projection of a vector on v vector
a = np.array([20,10,50])
v = np.array([70,40,66])

#magnitude of v vector
magnitude_v_vector = np.sqrt(sum(v**2))
proj_of_a_vector_on_v_vector = (np.dot(a,v) / magnitude_v_vector** 2) * v
print(proj_of_a_vector_on_v_vector)

