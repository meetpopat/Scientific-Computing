# Question 8_b

n = int(input("Enter the size of th square matrix:"))
A = []
for i in range(n):
    row = list(map(float, input("Enter elements of row (Space seperated):").split()))
    A.append(row)

b = list(map(float, input("Enter elements of b(Space seperated):").split()))
x = [0] * n
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

    for i in range(k+1, n):
        amult = A[l[i]][k] / A[l[k]][k]
        A[l[i]][k] = amult
        for j in range(k+1, n):
            A[l[i]][j] -= amult * A[l[k]][j]

for k in range(n - 1):
    for i in range(k+1, n):
        b[l[i]] -= A[l[i]][k] * b[l[k]]

x[n - 1] = b[l[n - 1]] / A[l[n - 1]][n - 1]
for i in range(n - 2, -1, -1):
    sum = b[l[i]]
    for j in range(i + 1, n):
        sum -= A[l[i]][j] * x[j]
    x[i] = sum / A[l[i]][i]
print(x)