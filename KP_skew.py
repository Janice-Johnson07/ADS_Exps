import numpy as np

def pearson_coefficient_skewness(x):
    x_mean =  np.mean(x)
    x_median = np.median(x)
    x_std = np.std(x)

    skewness = 3 * (x_mean - x_median) / x_std

    return skewness

x = np.array([1,2,3,4,5,6,7,8,9,10])

skewness = pearson_coefficient_skewness(x)
print("KP's coefficient of skewness is:",skewness)

    
