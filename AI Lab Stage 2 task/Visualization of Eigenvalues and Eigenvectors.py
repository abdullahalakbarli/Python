import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4, 1],
              [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

plt.figure(figsize=(8, 8))
ax = plt.gca()

plt.xlim(-5, 5)
plt.ylim(-5, 5)

origin = [0, 0]

for i in range(len(eigenvalues)):
    ax.quiver(*origin, eigenvectors[0, i], eigenvectors[1, i], angles='xy', scale_units='xy', scale=1, color=f'C{i}', lw=2, label=f'Eigenvector {i+1}')

for i in range(len(eigenvalues)):
    transformed_vector = np.dot(A, eigenvectors[:, i])
    ax.quiver(*origin, transformed_vector[0], transformed_vector[1], angles='xy', scale_units='xy', scale=1, color=f'C{i}', linestyle='dashed', lw=2, alpha=0.6)

ax.set_aspect('equal')
plt.grid(True, linestyle='--', alpha=0.5)
plt.axhline(0, color='black',linewidth=0.8)
plt.axvline(0, color='black',linewidth=0.8)

ax.spines['left'].set_color('gray')
ax.spines['bottom'].set_color('gray')

plt.legend(loc='upper right', fontsize=12)
plt.title('Eigenvalues və Eigenvectors Vizualizasiyası', fontsize=14, fontweight='bold')

plt.xticks(np.arange(-5, 6, 1), fontsize=12)
plt.yticks(np.arange(-5, 6, 1), fontsize=12)
plt.show()
