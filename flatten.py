# .ravel() --> view
# .flatten()  --> copy
# .reshape() --> view or copy (depends on memory layout)
import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:")
print(array)
ravel_array = array.ravel()
flatten_array = array.flatten()
reshaped_array = array.reshape((3, 2))
print(ravel_array)
print(flatten_array)
print(reshaped_array)
 

age = 20
s = "Adult"  if age >=18 else "Minor"
print(s)

