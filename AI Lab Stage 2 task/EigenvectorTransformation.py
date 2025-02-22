import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, 1],
              [1, 3]])

vectors = np.array([[1, 0], [0, 1], [1, 1], [-1, 1], [2, -1]])
transformed_vectors = np.dot(A, vectors.T).T

eigenvalues, eigenvectors = np.linalg.eig(A)
fig, ax = plt.subplots(figsize=(7,7))
original_color = '#7EBDC2'
transformed_color = '#F46036'

for v in vectors:
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, 
              color=original_color, alpha=0.7, linewidth=2)
    
for v in transformed_vectors:
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, 
              color=transformed_color, alpha=0.9, linewidth=2)

eigenvector_colors = ['blue', 'green']
scale_factors = [0.5, 2] 
for i in range(len(eigenvectors.T)):
    ev = eigenvectors[:, i] * eigenvalues[i] 
    ax.quiver(0, 0, ev[0], ev[1], angles='xy', scale_units='xy', scale=1, 
              color=eigenvector_colors[i], alpha=1, linewidth=3, label=f"Eigenvector {i+1} (Original)")

    for sf in scale_factors:
        ev_scaled = ev * sf
        ax.quiver(0, 0, ev_scaled[0], ev_scaled[1], angles='xy', scale_units='xy', scale=1, 
                  color=eigenvector_colors[i], alpha=0.5, linewidth=2, linestyle='dotted', 
                  label=f"Eigenvector {i+1} (Eigenvalue {sf})")

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axhline(0, color='black', linewidth=0.6, linestyle='dotted')
ax.axvline(0, color='black', linewidth=0.6, linestyle='dotted')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc="upper left")

plt.show()
