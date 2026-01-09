import numpy as np

# np.concatenate((array1,array2), axis = 0)

arr1 = np.array([[1,2,3],[5,6,7]])
arr2 = np.array([[4,5,6],[10,20,30]])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)