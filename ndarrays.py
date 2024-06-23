import numpy as np

a = np.array([1, 2])
print(a.shape) # -> (2,) | It's simple 1D dimensional array
# If we want multi-dimensional arrays
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b) # [[1, 2]
#           [3, 4]]
print(b.shape) # -> (2, 3) 1st - number of rows 2nd - number of columns

# To ACCESS
print(b[0]) # -> [1 2 3] accesses to 1st row
print(b[0][0]) # -> 1 accesses to 1st item of 1st row
print(b[:, 0]) # -> [1 4] first item of every row

# To transpose the array
print(b.T) # -> [[1 4] [2 5] [3 6]]