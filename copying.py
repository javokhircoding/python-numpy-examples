import numpy as np

a = np.array([1, 2, 3])
b = a
b[0] = 42
print(b) #absolutly it returns [42 2 4] BUT,
print(a) #it also returns [42 2 4] and you have not changed it

# the reason is the objects are still reference to the same memory, bucouse you just "equaled" them
# if we want diffirent memories and truly copy you can use copy method

v = np.array([1, 2, 3])
p = v.copy()
p[0] = 42
print(v) 
print(p) # NOw it works