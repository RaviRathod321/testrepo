import numpy as np

# ndarray.reshape
# ndarray.sum
# ndarray.mean
# ndarray.min
# ndarray.max
# ndarray.argmax
# ndarray.argmin
a = np.array([1, 2, 3, 4, 5, 23, 7, 8])
# print(a.reshape(2, 4))
#a = np.array([[1, 2],
#             [7, 8]])
#print(a.sum())
#print(a.max(axis=1))
#print(a.argmax()) #returns the value of the maximum number
print(a.argmin())