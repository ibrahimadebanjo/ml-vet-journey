import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.quiver(0,0,4,5, scale_units = "xy", angles = "xy", scale = 3, color = "b")
plt.quiver(0,0,-3,-6, scale_units = "xy", angles = "xy", scale = 3, color = "y")
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()