import numpy as np

a = np.array([1, 2, 3])

# Accessing some functions
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

# Accessing to specific element -- Just as standart python
print(a[0])
a[0] = 10
print(a[0])

# Some mathematical operatoins
print(a)
b = a * np.array([2, 0, 2]) #It multiplies with eacj unique elements, like: 1*2 2*0 3*2
print(b)

# Simple difference between python standart arrays and numpy array
l = [1, 2, 3]   # -> output: [1, 2, 3]
a = np.array([1, 2, 3])   # -> output: [1 2 3]

# Adding elements to array | Standart array
l.append(4) # But it doesn't work with numpy
l = l + [4] # It doesn't work

a = a + np.array([4]) # It works, but, as another function -> output: [5 6 7]
# And it's called BROADCAST method

# Another function
l = l * 2 # It just repeats for 2 times | [1, 2, 3, 1, 2, 3]
a = a * 2 # Then it multiplies the each element | [2 4 6]


# DOT PRODUCT
# IN standart python arrays
l1 = [1, 2, 3]
l2 = [4, 5, 6]
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot) # -> 32
# But it's much easier in numpy
a1 = np.array(l1)
a2 = np.array(l2)
dot = np.dot(a1, a2)
print(dot) # -> 32
# OR
sum1 = a1 * a2
dot = np.sum(sum1)
print(dot) # -> 32

# OR another awasome choice
dot = (a1 * a2).sum() # You just have to call
print(dot)
 
# MORE EASIER???? Absolutly!
dot =  a1 @ a2
print(dot) # -> 32