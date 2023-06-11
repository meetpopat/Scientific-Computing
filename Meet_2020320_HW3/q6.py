import numpy as np


def power_iteration(A, x):
    for i in range(1, 100):
        y = np.matmul(A, x)
        x = y / np.linalg.norm(y, ord=np.inf)
    a1 = np.linalg.norm(y, ord=np.inf)
    return [a1, x]


def reverse_iteration(A, x):
    for i in range(1, 101):
        y = np.linalg.solve(A, x)
        x = y / np.linalg.norm(y, ord=np.inf)
    a2 = 1 / np.linalg.norm(y, ord=np.inf)
    return [a2, x]


A = np.array([[2, 3, 2], [10, 3, 4], [3, 6, 1]])
b = np.array([0, 0, 1])
X = b.T

l1 = power_iteration(A, X)

print("Normalised Power Iteration Eigenvalue is :", l1[0])
print("Normalised Power Iteration Eigenvector are", l1[1])

l2 = reverse_iteration(A, X)

print("\nInverse Iteration Eigenvalue is :", l2[0])
print("Inverse IterationEigenvector is :", l2[1])

print("\nActual Eigenvalues is :", np.linalg.eig(A)[0])
print("Actual Eigenvectors are : \n", np.linalg.eig(A)[1])