import numpy as np
import scipy as sp
import numpy.linalg as npla
import scipy.linalg as spla

for i in range(6, 16):
    exponent = pow(10, -i)
    matrixA = np.array([[1,1], [exponent,0], [0,exponent]], dtype = float)
    ArrayB = np.array([[-exponent], [1+exponent], [1-exponent]], dtype = float)

    ans = npla.solve(np.matmul(matrixA.T, matrixA), np.matmul(matrixA.T, ArrayB))
    print(ans)
