import numpy as np

# Create arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Basic operations
print("Array A:", a)
print("Array B:", b)
print("\nA + B =", a + b)
print("A * B =", a * b)
print("A mean =", np.mean(a))
print("B standard deviation =", np.std(b))

# Reshaping
matrix = np.arange(1, 10).reshape(3, 3)
print("\nMatrix:\n", matrix)

# Matrix operations
print("\nMatrix transpose:\n", matrix.T)
print("Matrix sum =", np.sum(matrix))
print("Matrix dot product:\n", np.dot(matrix, matrix))
