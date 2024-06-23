import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]])
a = np.array([[1, 0, 1]])
y = x + a
print(y) # As we said earlier it just adds the number index by index

# calculate the sum
a = np.array([[7, 8, 9, 10, 11, 12, 13], [17, 18, 19, 20, 21, 22, 23]])
print(a)
print(a.sum())
print(np.sum(a))