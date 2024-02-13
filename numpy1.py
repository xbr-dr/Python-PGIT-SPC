# the NumPY tutorial, first import the library as np
# we use aliasing for our convenience
import numpy as np

# let's create two lists for later use
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [9, 10, 11, 12, 13, 14, 15, 16]
# to convert them into 2-dimensional array
arr = np.array([l1, l2])
# to understand the slicing (start:end:step), used for 2-dim here
# left blank intentionally for default values giving us all elements with step=1
print(arr[::, ::])
# we can print the type of the array created
print(type(arr))
# shape gives us the mathematical dimension of the matrix or array formed
print(np.shape(arr))
# to know the total no. of elements in the array
print(np.size(arr))
# ndim tells us the array dimensions whether 2-dim, 3-dim, etc
print(np.ndim(arr))
# the data type used in the array
print(arr.dtype)
# some mathematical functions to get the min, sum, diff, etc.
print(np.min(arr))
print(np.max(arr))
print(np.sum(arr))
print(np.diff(arr))
# to convert the array in matrix (not important)
print(np.mat(arr))
# transpose of the above matrix
print(np.transpose(arr))
# creating arrays using numpy functions like arange, zeros, ones, full, etc.

print(np.arange(0, 6))
print(np.zeros((6, 2, 2), dtype=int))
print(np.ones((6, 2, 2), dtype=int))
print(np.full((6, 8), 8, dtype=int))
# we can reshape a particular array like:-
print(np.arange(9).reshape(3, 3))
# more methods on array like sort, power, concatenate, cross, etc.
t1 = [5, 1, 8, 64, 7, 6]
print(np.array(t1))
t = np.sort(t1)
print(t)
t2 = np.array(t1)
p = np.power(t, [2])
print(p)
a = np.array([1, 2])
b = np.array([6, 7])
print(np.concatenate((a, b)))
print(np.cross(a, b))
# we can use more methods and functions from NumPy....
# visit the GitHub repository for more programs and material
# Xbr_Dr
# https://github.com/xbr-dr/Python-PGIT-SPC/main/numpy1.py
