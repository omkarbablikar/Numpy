import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2])


aar3 = arr1 + arr2
print(aar3)

# This will raise a ValueError because the shapes (2,3) and (2,) are not compatible for broadcasting.
# ValueError: shapes (2,3) and (2,) not aligned: 3 (dim 1) != 2 (dim 0) 