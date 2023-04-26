import numpy as np


def spearman_correlation(x,y):
    x_rank = np.argsort(np.argsort(x))
    y_rank = np.argsort(np.argsort(y))

    r = np.corrcoef(x_rank , y_rank) [0 , 1]

    n = len(x)
    rho = 1 - 6 * np.sum((x_rank - y_rank) **2)/(n*(n**2 - 1))
    return rho

x = np.array([1 ,2,3,4,5])
y = np.array([2,4,6,8,10])

rho = spearman_correlation(x,y)
print("Spearman:",rho)
                 
                 
