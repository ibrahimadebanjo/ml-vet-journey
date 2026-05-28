import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.quiver(0,0,2,3, scale_units = "xy", angles = "xy", scale = 3, color = "b")
plt.quiver(0,0,3,-2, scale_units = "xy", angles = "xy", scale = 3, color = "y")
plt.quiver(0,0,5,1, scale_units = "xy", angles = "xy", scale = 3, color = "r")

plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()