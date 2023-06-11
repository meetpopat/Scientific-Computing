import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npla

def start(x_noisy, D_matrix):
    lambda_list = [1, 100, 10000]

    plt.figure()
    lamda= None
    is_noisy=True
    if not is_noisy:
        plt.plot(np.arange(1, 1 + len(solution)), solution,
        color=(0.0, 0.5, 0.5), label="Lambda="+str(lamda))
        
        plt.xlabel("$n$", fontsize=14)
        plt.ylabel("$x$", fontsize=14)
    else:
        plt.plot(np.arange(1, 1 + len(x_noisy)), x_noisy,
        color=(0.5, 0.5, 0.5), label="Noisy Signal")

        plt.xlabel("$n$", fontsize=14)
        plt.ylabel("$x_{noisy}$", fontsize=14)
    
    plt.legend(loc="best")
    plt.gcf().tight_layout()


    for lamda in lambda_list:
        D_matrix = np.matmul(D_matrix.T, D_matrix)
        D_matrix = lamda*D_matrix
        I = np.identity(1000)
        A_matrix = I + D_matrix
  
        solution = npla.solve(A_matrix, x_noisy)
        
        is_noisy=False
        plt.figure()
        if not is_noisy:
            plt.plot(np.arange(1, 1 + len(solution)), solution,
            color=(0.0, 0.5, 0.5), label="Lambda="+str(lamda))
        
            plt.xlabel("$n$", fontsize=14)
            plt.ylabel("$x$", fontsize=14)
        else:
            plt.plot(np.arange(1, 1 + len(x_noisy)), x_noisy,
            color=(0.5, 0.5, 0.5), label="Noisy Signal")

            plt.xlabel("$n$", fontsize=14)
            plt.ylabel("$x_{noisy}$", fontsize=14)
    
        plt.legend(loc="best")
        plt.gcf().tight_layout()
    
    plt.show()    
        
D_matrix1=np.zeros([999, 1000])
np.fill_diagonal(D_matrix1, -1)
for i in range(998):
    D_matrix1[i,i+1] = 1
    D_matrix1[998, 999] = 1

x_noisy = np.loadtxt("hw2_data_denoising.txt")
start(x_noisy, D_matrix1)



