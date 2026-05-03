import numpy as np

A = np.array([[10, -1, 2],
              [-1, 11, -1],
              [2, -1, 10]])

b = np.array([6, 25, -11])

x = np.zeros(3)

for _ in range(25):
    for i in range(3):
        s = sum(A[i][j] * x[j] for j in range(3) if j != i)
        x[i] = (b[i] - s) / A[i][i]

print("Solution:", x)
