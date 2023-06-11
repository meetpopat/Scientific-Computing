import numpy as np
import numpy.linalg as npla
import scipy.linalg as spla

A = np.array([[2, 3, 2], [10, 3, 4], [3, 6, 1]])
mu = A[2,2]
I = np.zeros([3,3])
I[0][0] = 1
I[1][1] = 1
I[2][2] = 1


k=1
while(k<1000):
    Q,R  = spla.qr(A-mu*I)
    A = np.matmul(R, Q) + mu*I
    k=k+1
print("Eigenvalue from Q6 is :", [A[0,0], A[1,1], A[2,2]])
print("Actual Eigenvalue from Q6 is :", npla.eig(A)[0])

A = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
mu = A[2,2]
I = np.identity(3)

j=1
while(j<100):
    Q, R = spla.qr(A-mu*I)
    A = np.matmul(R, Q) + mu*I
    j=j+1
print("\nEigenvalue from Q7 is :", [A[0,0], A[1,1], A[2,2]])
print("Actual Eigenvalue from Q7 is :",npla.eig(A)[0])