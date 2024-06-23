import numpy as np

 
a = np.random.random((3, 2)) # it generates random numbers between 0 and 1 (0-1) and as we said it has 3 rows and per 2 columns
print(a)

b = np.random.randn(3, 2)  # normal/Gaussion
print(b.mean(), b.var())

# And there is also funcktion is meant to generate integers
i = np.random.randint(3, 10, size=(3, 3))  # (start, stop) - 3 is start 10 is stop and size is shape
print(i) # now we got normal int arrays


# To get random choice
c = np.random.choice(5, size=10) # it randomly choices elements between 0 and 5 and it has 10 choices
print(c) # -> [3 4 2 2 4 3 3 2 0 3] 

#WE CAN ALSO USE IT WITH GIVEN LIST
c2 = np.random.choice([1, 3, 5, 66, 23, 21], size=10) # and it has 10 choices
print(c2)