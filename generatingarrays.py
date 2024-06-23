import numpy as np

a = np.zeros((2, 3))
print(a) # it just returns rezos with this shape (2, 3)
# ALSO
b = np.ones((2, 3))
print(b) # You notice that default datatype is float

# To get specific values
v = np.full((2, 3), 5.0)
print(v) # It returns only 5 -> [[5. 5. 5.] [5. 5. 5.]] all filled with 5s


# IF WE WANT TO GET MATRIX
m = np.eye(3)
print(m) # it returns something like this:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# we aslo know arange method
ar = np.arange(20)
print(ar) # just returns 0 to 19 with 1 demensional shape

lin = np.linspace(0, 10, 5) #1st - number of start | 2nd - number of stop | 3rd - steps and it returns
print(lin) # -> [ 0.   2.5  5.   7.5 10. ]