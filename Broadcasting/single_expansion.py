import numpy as np

result = np.array([1, 2, 3]) + 5
print(result)

# Output: [6 7 8]

array = np.array([[1, 2, 3], [4, 5, 6]])    
result = array * np.array([10, 20, 30])
print(result)
# Output:
# [[10 40 90]
#  [40 100 180]]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix + np.array([[100], [200], [300]])
print(result)
# Output:
# [[101 102 103]
#  [204 205 206]
#  [307 308 309]]
vector = np.array([1, 2, 3])
result = vector + np.array([[10], [20], [30]])  
print(result)
# Output:
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]
