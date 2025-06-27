#Q1.Create a numpy array
import numpy as np
a = np.empty((4,2))
print("Empty Array:\n",a)
b = np.full((4,2),7)
print("Full array of 7:\n",b)
c = np.zeros((3,5))
print("Zero array:\n",c)
d = np.ones((4,3,2))
print("Array of ones:\n",d)

#Q2 2d array 3x3 values ranging from 2 to 10
arr = np.random.randint(2,11, size =(3,3))
print("2d array:\n",arr)

#Q3 null vector
nv = np.zeros(10)
print(nv)
nv[5]=11
print(nv)

#Q4 reverse an array
arr= np.array([1,2,3,4,5])
print("Reverse array:",arr[::-1])

#Q5 array to floating type
arr = np.array([1,2,3,4,5],dtype="float" )
print(arr)
print(arr.dtype)

