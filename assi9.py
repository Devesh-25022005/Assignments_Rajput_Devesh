import numpy as np
#Q1 combine 1d and 2d array
arr1 = np.array([1,2,3,4])
arr2 = np.array([[4,5,6],[7,8,9]])
res = np.append(arr1,arr2)
print("Result  of Comination:",res)

#Q2)Flatten 2d into 1d array
b = np.array([[10,20,30],[40,50,60]])
flatten = b.reshape(-1)
print(flatten)


#Q3)Reverse numpy array
c = np.array([[1,2,3],[4,5,6]])
reverse = np.flip(c)
print(reverse)

#Q4 
d = np.array([[99,101,234,65],[1,34,567,89]])
print("Maximum:",d.max())
print("Minimum:",d.min())
print("Shape of the array:",d.shape)
print("Element specific to position: row 2 1st element",d[1,0])
#print each element
for x in np.nditer(d):
    print(x)

#sum 
sum=0
for rows in d:
    for x in rows:
        sum+=x
print("Sum of values:",sum)



a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])

print(a + b)
print(a-b)
print(a * b)
print(a / b)
