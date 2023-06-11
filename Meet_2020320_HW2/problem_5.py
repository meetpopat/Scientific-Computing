
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npla


def start(t, y):

    plt.figure()
    plt.plot(t, y, 'bo', ms=2.5)
    plt.title("Original")
    plt.grid(True)
    plt.xlabel("$t_i$", fontsize=14)
    plt.ylabel("$f(t_i)$", fontsize=14)
    plt.gcf().tight_layout()

    A_matrix = np.ones([50, 2], dtype=float)
    for i in range(len(t)):
        A_matrix[i,0] = t[i]
    B_matrix = np.zeros([50, 1], dtype=float)
    for i in range(len(y)):
        B_matrix[i, 0] = np.log(y[i]/(1-y[i]))

    x1 = npla.solve(np.matmul(A_matrix.T, A_matrix), np.matmul(A_matrix.T, B_matrix))
    x2 = npla.lstsq(A_matrix, B_matrix, rcond=None)[0]


    error_from_solve = npla.norm(B_matrix - np.matmul(A_matrix, x1), 2)
    error_from_lstsq = npla.norm(B_matrix - np.matmul(A_matrix, x2), 2)

    print("Error solve:", error_from_solve)
    print("Error lstsq:", error_from_lstsq)


    y1=np.matmul(A_matrix, x1)   
    for i in range(0 ,50):
        temp = pow(np.e, y1[i])     
        y1[i] = temp/(temp +1)      
    
    plt.figure()
    plt.plot(t,  y1, 'bo', ms=2.5)
    plt.title("solve method")
    plt.grid(True)
    plt.xlabel("$t_i$", fontsize=14)
    plt.ylabel("$f(t_i)$", fontsize=14)
    plt.gcf().tight_layout()

    y2=np.matmul(A_matrix, x2)   
    for i in range(0 ,50):
        temp = pow(np.e, y1[i])     
        y2[i] = temp/(temp +1)      
    
    plt.figure()
    plt.plot(t,  y2, 'bo', ms=2.5)
    plt.title("lstsq method")
    plt.grid(True)
    plt.xlabel("$t_i$", fontsize=14)
    plt.ylabel("$f(t_i)$", fontsize=14)
    plt.gcf().tight_layout()
    

t, y = np.loadtxt("hw2_data_ty.txt").T
start(t, y)
plt.show()
