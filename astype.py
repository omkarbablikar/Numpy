import numpy as np

array = np.array([10.5, 20.3, 30.7, 40.2, 50.9])
print(array.dtype)
int_array = array.astype(int)
print(int_array)
print(int_array.dtype)