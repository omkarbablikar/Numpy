import numpy as np

temperature = np.array([22.5, 23.0, 21.8, 22.1, 23.3])

average_temp = np.mean(temperature)
print(f"The average temperature is: {average_temp:.2f}C")


matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(matrix)
print("Matrix shape:", matrix.shape)
print("Matrix sum:", np.sum(matrix))


import numpy as np

array = np.array([10, 20, 30, 40, 50])
print("Original array:", array)


zeros_array = np.zeros(3)
print("Array of zeros:", zeros_array)

ones_array = np.ones(3)
print("Array of zeros:", ones_array)

full_array = np.full((2,2),7)
print(full_array)

print(np.arange(1,10,2))

identity_matrix = np.eye(10)
print(identity_matrix)