import numpy as np

# np.delete(array, index, axis= None)

arr = np.array([1,2,3,4,5])

aaar = np.delete(arr, 2)
print(aaar)


arr2ed = np.array([[10,20,30],[40,50,60]])

arr = np.delete(arr2ed, 0, axis=1)
print(arr)