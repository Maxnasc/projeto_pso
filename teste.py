import numpy as np

matriz1 = np.arange(6, 11)
matriz1 = matriz1.T
matriz2 = np.array([1, 2, 3, 4, 5])
matriz5 = matriz1 * matriz2
matriz6 = matriz1 @ matriz2
print(matriz5)
print(matriz6)