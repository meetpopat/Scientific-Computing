import numpy as np

x = 1
for j in range(0, 20):
    x = (np.pi / 4 + 2 * np.pi * (10 ** j))
    print("(x, tan(x)) = (%1.16f, %1.16f)" % (x, np.tan(x)))
    print("(x, tan(x)) = (% 1.16f, % 1.16f)" % (x, np.tan(x)))
    print("Relative Condition No.:", abs(x / (np.sin(x) * np.cos(x))))
    print("Absolute Condition No.:", abs(1 / (np.cos(x) ** 2)))
    print("input x differs from 1:", abs(x - 1))
