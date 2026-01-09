import numpy as np
# np.insert(array, index, values, axis= None)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
new_arr = np.insert(arr, 1, 10)
print(new_arr)


arr2 = np.array([['a','b','c'],['d','e','f']])
new_arr2 = np.insert(arr2, 2, 'v', 1)
print(new_arr2)