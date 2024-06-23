import numpy as np

# First we do it manually (picture is on the telegram)
A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])

X = np.linalg.inv(A).dot(b)
print(X)
# This is actually corect but this is not the best way to solve it

# HERE IS BETTER VERSION
x = np.linalg.solve(A, b)
print(x)

# The result is [1500.  700.]