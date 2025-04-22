import numpy as np

# Create two arrays of the same shape
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("Array a:", a)
print("Array b:", b)

# Element-wise operations
print("\nElement-wise Addition:", a + b)
print("Element-wise Subtraction:", a - b)
print("Element-wise Multiplication:", a * b)
print("Element-wise Division:", a / b)

# Dot Product
dot_product = np.dot(a, b)
print("\nDot Product:", dot_product)

# Cross Product
cross_product = np.cross(a, b)
print("Cross Product:", cross_product)
