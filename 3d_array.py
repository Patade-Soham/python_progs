import numpy as np

# 1D Array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# 2D Array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

# 3D Array
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:")
print(array_3d)

# Basic Operations

# Reshaping
reshaped_array = array_1d.reshape((5, 1))
print("\nReshaped 1D Array to 2D (5x1):")
print(reshaped_array)

# Slicing 2D Array
slice_2d = array_2d[:, 1]  # All rows, 2nd column
print("\nSliced 2D Array (All rows, 2nd column):")
print(slice_2d)

# Indexing 3D Array
element_3d = array_3d[1, 0, 1]  # 2nd block, 1st row, 2nd column
print("\nIndexed Element from 3D Array (array_3d[1, 0, 1]):")
print(element_3d)
