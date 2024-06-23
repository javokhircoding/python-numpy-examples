import numpy as np
# How we can load data from CSV files into numpy arrays?

# Loading ways: np.loadtxt, np.genfromtxt
data = np.loadtxt('spambase.csv', delimiter=",", dtype=np.float32)
print(data)
print(data.shape)