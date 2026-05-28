import numpy as np
#projection of a vector on v vector
a = np.array([2,5])
v = np.array([8,-6])

#magnitude of v vector
magnitude_v_vector = np.sqrt(sum(v**2))
proj_of_a_vector_on_v_vector = (np.dot(a,v) / magnitude_v_vector** 2) * v
print(proj_of_a_vector_on_v_vector)

