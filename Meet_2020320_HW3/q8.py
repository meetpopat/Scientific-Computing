import numpy as np

A = np.array([[2, 3, 2], [10, 3, 4], [3, 6, 1]])
x = np.array([[1], [0], [1]])

k = 0
I = np.identity(3)

while True:
    if k == 1000:
        break
    k = k + 1
    ans = np.matmul(np.matmul(x.T, A), x) / np.matmul(x.T, x)
    y = np.linalg.solve(A - ans * I, x)
    x = np.linalg.norm(y, ord=np.inf)
    x = y / x

print("Rayleigh Quotient:")
print('Eigenvalue:>', ans[0][0])
print('Eigenvalue:', x)

print("Library Routine :")
print(np.linalg.eigh(A))

