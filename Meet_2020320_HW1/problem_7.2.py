import math

k = 1
n = 5000
total = 0

for k in range(1, n + 1):
    total = total + (1 / k)
    if k % 100 == 0:
        print(total - math.log(k + 1 / 2))
