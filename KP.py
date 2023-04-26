import numpy as np

def persons_coefficient_correlation(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = np.std(x)
    y_std = np.std(y)

    covariance = np.sum((x - x_mean) * (y - y_mean))/len(x)

    r = covariance / (x_std * y_std)

    return r

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

r = persons_coefficient_correlation(x,y)

print("KP's coefficient of correlartion is:",r)
                            
