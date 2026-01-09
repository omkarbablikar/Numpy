import numpy as np

array_2d = np.array([[1,2,3], [4,5,6]])
print("2D Array:")
print(array_2d.shape) #dimensions of the array
print(array_2d.size) #total number of elements 
print(array_2d.ndim) #number of array dimensions    

array_3d = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(array_3d.ndim)
print(array_3d.dtype)