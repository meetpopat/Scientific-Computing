# Question 8_a

n = int(input("Enter the size of th square matrix:"))
A = []
for i in range(n):
    row = list(map(float, input("Enter elements of row (Space seperated):").split()))
    A.append(row)

b = list(map(float, input("Enter elements of b(Space seperated):").split()))

x = [0] * n

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
    print(x)
