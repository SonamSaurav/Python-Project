import numpy as np

# Create a 2x2 matrix
matrix_a = np.array([[1, 2], [3, 4]])

# (i) Data type
print("Data type of the matrix:", matrix_a.dtype)

# (ii) Rank of the matrix
print("Rank of the matrix:", np.linalg.matrix_rank(matrix_a))

# (iii) Order of the matrix
print("Order of the matrix:", matrix_a.shape)

# (iv) Convert the matrix into 1-D array
flat_array = matrix_a.flatten()
print("1-D array representation:", flat_array)

# Create another 2x2 matrix
matrix_b = np.array([[5, 6], [7, 8]])

# (v) Perform addition, subtraction, and division operations
matrix_sum = matrix_a + matrix_b
matrix_diff = matrix_a - matrix_b
matrix_div = matrix_a / matrix_b

print("\nMatrix Addition:")
print(matrix_sum)

print("\nMatrix Subtraction:")
print(matrix_diff)

print("\nMatrix Division:")
print(matrix_div)
