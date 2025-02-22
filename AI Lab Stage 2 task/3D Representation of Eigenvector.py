import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vectors_3D_modern = [
    np.array([0.5, 0.2, 0.7]),
    np.array([-0.3, 0.8, 0.5]),
    np.array([0.7, -0.6, 0.1])
]

transformed_vectors_3D_modern = [
    np.array([0.6, 0.1, 0.8]),
    np.array([-0.5, 0.7, 0.6]),
    np.array([0.8, -0.4, 0.2])
]

longest_eigenvector = np.array([1.0, 0.5, 0.3])  

scale_factors = [0.5, 1, 2]  
alpha_values = [1, 0.75, 0.5]  

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

for v in vectors_3D_modern:
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='#B0B0B0', alpha=0.6, linewidth=1.5)

for v in transformed_vectors_3D_modern:
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='#005F99', alpha=0.9, linewidth=3)

for i, sf in enumerate(scale_factors):
    ev_scaled = longest_eigenvector * sf
    ax.quiver(0, 0, 0, ev_scaled[0], ev_scaled[1], ev_scaled[2],
              color='green', alpha=alpha_values[i], linewidth=3, label=f"Eigenvalue ({sf})")

ax.set_xlim([-1, 1.5])
ax.set_ylim([-1, 1.5])
ax.set_zlim([-1, 1.5])

ax.set_xlabel('X', fontsize=12, fontweight='bold', color='#333')
ax.set_ylabel('Y', fontsize=12, fontweight='bold', color='#333')
ax.set_zlabel('Z', fontsize=12, fontweight='bold', color='#333')
ax.set_title("3 Scaled Versions of the Longest Eigenvector", fontsize=14, fontweight='bold', color='#222')

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.legend(loc="upper left")
plt.show()
