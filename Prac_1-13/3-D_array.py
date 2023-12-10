import numpy as np

# Create a 3-D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# (i) Transpose of a matrix
transposed_array = np.transpose(array_3d)
print("Original 3-D array:")
print(array_3d)

print("\nTransposed 3-D array:")
print(transposed_array)

# (ii) Create another 3-D array for matrix multiplication
array_3d_multiply = np.array([[[2, 0], [1, 1]], [[1, 2], [0, 1]]])

# Perform matrix multiplication
result_matrix_multiply = np.matmul(array_3d, array_3d_multiply)

print("\nMatrix for Multiplication:")
print(array_3d_multiply)

print("\nResult of Matrix Multiplication:")
print(result_matrix_multiply)
