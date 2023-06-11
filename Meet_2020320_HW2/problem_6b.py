import numpy as np
import numpy.linalg as npla
import scipy as sp
import scipy.linalg as spla


for i in range(6, 16):
    exponent = pow(10, -i)
    matrixA = np.array([[1,    1], [exponent, 0], [0, exponent]], dtype = float)
    ArrayB = np.array([[-exponent], [1+exponent], [1-exponent]], dtype = float)

    matrixQ, matrixR = npla.qr(matrixA)
    ans = spla.solve_triangular(matrixR, np.matmul(matrixQ.T, ArrayB))
    print(ans)

