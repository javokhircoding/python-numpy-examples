import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)

b = a[0, 1:3]
print(b) #-> [2 3]

b = a[0, 1]
print(b) #-> 2 | zow zero, column 1 so it prints out 2


# BOOLEAN INDEXING
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a) # -> [[1 2] [3 4] [5 6]]

bool_idx = a > 2
print(bool_idx) # -> [[False False] [True True] [True True]] it just checks the condition

print(a[bool_idx]) # -> [3 4 5 6] we only get the elements that greater than 2 | a > 2
print(a[a>2]) # -> returns the same result
# OR more advanced way
b = np.where(a>2, a, -1) # a > 2 is condition, a is the list that shoul be checked, 
                         # -1 is the deafult number that automatically puts in false condition
print(b) # -> [[-1 -1] [3 4] [5 6]]


# FANCY INDEXING
a = np.array([10, 19, 30, 41, 50, 61])
print(a)
b = [1, 3, 5] 
print(a[b]) # it says print a arrays' b-indexing elements, it outputs: [19 41 61]

a = np.array([10, 19, 30, 41, 50, 61])
print(a)
even = np.argwhere(a%2==0).flatten()
print(a[even]) #-> [10 30 40] by a[even] it applies the even condition for a array


# RESHAPING ARRAYS
a = np.arange(1, 7)
print(a) # it return 1 to 6, 1 2 3 4 5 6
print(a.shape) #-> (6,)  it has 1 dimention
# now we can reshape it
b = a.reshape((2, 3))
print(b) #-> [[1 2 3] [4 5 6]] it reshaped it into 2 rows and 3 columns
print(b.shape) #-> (2, 3) it has 2 dimentions

b = a[np.newaxis, :]
print(b) # -> now it is [[1 2 3 4 5 6]] now it's a list of list
print(b.shape) # -> (1, 6)
# or 
b = a[:, np.newaxis]
print(b) # -> [[1] [2] [3] [4] [5] [6]]
print(b.shape) # -> (6, 1) 6 rows per one item