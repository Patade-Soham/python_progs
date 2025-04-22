import numpy as np
from scipy import stats

def analyze_array(data):
    data = np.array(data)
   
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data, ddof=1)  # Sample standard deviation
    variance = np.var(data, ddof=1)  # Sample variance
    correlation_matrix = np.corrcoef(data)  # Correlation coefficients
   
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Correlation Coefficients:\n{correlation_matrix}")
   
    return mean, median, std_dev, variance, correlation_matrix
