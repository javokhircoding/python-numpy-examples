import numpy as np

a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)  # column vector


# e_vec * e_val = A * e_vec
b = eigenvectors[:, 0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:, 0]
print(c)


# print(b==c) this is not correct way to compare it
# TRUE version is
print(np.allclose(b, c)) # And this returns true, becouse it's the correct way of comparing
