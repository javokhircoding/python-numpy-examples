import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

b = np.array([[5, 6]])
# Now if we want to put them together...
c = np.concatenate((a, b))
print(c) # now they are at the same array


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# hstack
c = np.hstack((a, b)) # it just added as highly stack, we also have vstack - vertically
print(c) # -> [1 2 3 4 5 6 7 8]
# vstack
p = np.vstack((a, b))
print(p) # -> [[1 2 3 4] [5 6 7 8]]