import numpy as np

x = np.array([1, 2])
print(x)
print(x.dtype) # -> int32 | it automatically figures out the data 

y = np.array([1.0, 2.5])
print(y.dtype) # -> float64 bucouse it is 1.0 or 2.5

# OR we can set the datatype ourselves
d = np.array([1.0, 2.0], dtype=np.int64)
print(d)
print(d.dtype) # -> it returns int64 after we set datatype