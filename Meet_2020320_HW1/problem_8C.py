import numpy as np
import numpy.linalg as npla


def withPartialPivoting(A, b, n):
    x = np.zeros((n, n))
    l = [0] * n
    s = [0] * n

    for i in range(n):
        l[i] = i
        smax = 0
        for j in range(n):
            smax = max(smax, abs(A[i][j]))
        s[i] = smax

    for k in range(n - 1):
        rmax = 0
        for i in range(k, n):
            r = abs(A[l[i]][k] / s[l[i]])
            if r > rmax:
                rmax = r
                j = i

        ltemp = l[k]
        l[k] = l[j]
        l[j] = ltemp

        for i in range(k + 1, n):
            amult = A[l[i]][k] / A[l[k]][k]
            A[l[i]][k] = amult
            for j in range(k + 1, n):
                A[l[i]][j] -= amult * A[l[k]][j]

    for k in range(n - 1):
        for i in range(k + 1, n):
            b[l[i]] -= A[l[i]][k] * b[l[k]]

    x[n - 1] = b[l[n - 1]] / A[l[n - 1]][n - 1]
    for i in range(n - 2, -1, -1):
        sum = b[l[i]]
        for j in range(i + 1, n):
            sum -= A[l[i]][j] * x[j]
        x[i] = sum / A[l[i]][i]

    return (x)


def withoutPartialPivoting(A, b, n):
    x = np.zeros((n, n))
    k = 0
    while k < n - 1:
        for i in range(k + 1, n):
            temp = A[i][k] / A[k][k]
            A[i][k] = temp
            for j in range(k + 1, n):
                A[i][j] -= temp * A[k][j]
            b[i] -= temp * b[k]
        k = k + 1

    if A[n - 1][n - 1] == 0:
        print("Determinant of A is zero hence no solution")
    else:
        x[n - 1] = b[n - 1] / A[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            temp2 = b[i]
            for j in range(i + 1, n):
                temp2 = temp2 - A[i][j] * x[j]
            x[i] = temp2 / A[i][i]
    return (x)


def matrix_input(n, sno):
    x_cap = np.ones((n, n))
    if sno == 1:
        matrix_a = np.random.random_sample((n, n))
        matrix_b = np.matmul(matrix_a, x_cap)

    elif sno == 2:
        matrix_a = np.zeros((n, n))  # 1/i+j-1
        for i in range(n):
            for j in range(n):
                matrix_a[i][j] = 1 / (i + j + 1)
        matrix_b = np.matmul(matrix_a, x_cap)

    else:
        matrix_a = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if i>=j:
                    matrix_a[i][j] = 1
                else:
                    matrix_a[i][j] = -1
        matrix_b = np.matmul(matrix_a, x_cap)

    return matrix_a, matrix_b, x_cap


n_test_values = [10, 20, 30, 40]
s_no = [1, 2, 3]
for no in s_no:
    for n in n_test_values:
        if no == 1:
            print("Random Matrix-")
        elif no == 2:
            print("Hilbert Matrix-")
        else:
            print("One/Minus One Matrix")

        matrix_a, matrix_b, x_cap = matrix_input(n, no)

        print("Before:", npla.cond(matrix_a, 2))
        withoutPP = withoutPartialPivoting(matrix_a, matrix_b, n)
        withPP = withPartialPivoting(matrix_a, matrix_b, n)

        print("n:", n)
        print("Condition number (np.linalg.cond):", npla.cond(matrix_a, 2))
        print("Error without pivoting algo:", npla.norm(withoutPP - x_cap, 2) / npla.norm(x_cap, 2))
        Ax = np.matmul(matrix_a, withoutPP)
        print("Residual from without pivoting algo:", npla.norm(matrix_b - Ax, 2) / npla.norm(matrix_b, 2))
        print("Error from partially-pivoted algo:", npla.norm(withPP - x_cap, 2) / npla.norm(x_cap, 2))
        Ax = np.matmul(matrix_a, withPP)
        print("Residual from partially-pivoted algo:", npla.norm(matrix_b - Ax, 2) / npla.norm(matrix_b, 2))
        print("Error from np.linalg.solve:", npla.norm(npla.solve(matrix_a, matrix_b) - x_cap, 2) / npla.norm(x_cap, 2))
        Ax = np.matmul(matrix_a, npla.solve(matrix_a, matrix_b))
        print("Residual from np.linalg.solve:", npla.norm(matrix_b - Ax, 2) / npla.norm(matrix_b, 2))
