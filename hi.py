
import numpy as np

hi = np.array([1, 2, 3, 4, 5])

print(hi)

print(type(hi))

hello = np.array((1,2,4))

print(hello)

dimend = np.array([[1,2,3,4],[3,4,5,6,7]])

print(dimend)

print(dimend.ndim)

arra = np.array([1,2,3,4], ndmin = 5)

print(arra)

print(arra.ndim)

list = np.array([1,5,6,7,7])

print(list[0])

print(list.dtype)

you = np.array([8,9,7,6,0], dtype = 'S')

print(you)

print(you.dtype)

copy = np.array([3,4,5,6])

copy1 = copy.copy()

copy[0] = 300

print(copy)

print(copy1)

process = np.array([[45,6,7,8],[64,67,23,56]])

print(process.shape)
