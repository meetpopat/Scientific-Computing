import numpy as np
import numpy.linalg as npla

A = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
I = np.zeros([3,3])
I[0][0] = I[1][1] = I[2][2] = 1

X = np.array([1, 1, 1])

i = 1
Y = 0
while i <= 99:
    Y = np.linalg.solve((A-2*I), X)
    X = Y/np.linalg.norm(Y, ord=np.inf)
    i += 1

a = 2 + 1/npla.norm(Y,ord=np.inf)

print("Eigenvalue is : ", a)
print("Eigenvector is : ", X)

print("\nAll Actual Eigenvalue is :", npla.eigh(A, 'U')[0])
print("All Actual Eigenvector are : \n", npla.eigh(A,'L')[1])