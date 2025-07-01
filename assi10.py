import numpy as np

#Q1
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
res = np.nan_to_num(arr, nan=0)
print(res)

#interchanging rows and col
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[:,[0,1,2]] = arr2d[:,[1,2,0]]
print(arr2d)
arr2d[[0,1,2],:] = arr2d[[1,2,0],:]
print(arr2d)

#Q2 move axes of 3d array
arr = np.array([
    [[1, 2], [3, 4]], 
    [[5, 6], [7, 8]]
])
transposed=arr.transpose(1,0,2)
print(transposed)

#Q3 Replace nan with avg
arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
avg = np.nanmean(arr)
res = np.nan_to_num(arr, nan=avg)
print(res)

#Q4
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])

# Replace negative values with 0
arr[arr < 0] = 0

print(arr)

#Q5  Q6 Q7
arr1 = np.array([3,4])
arr2 = np.array([1,0])
avg = arr1+arr2/2
print("Average:",avg)
arr1=np.array([[1,2,2,3,4,5],[1,2,2,8,0,5]])
arr2=np.array([[1,2,2],[1,2,5]])
print("Mean of arr1",np.mean(arr1))
print("Median of arr1",np.median(arr1))
print("Mean of arr2",np.mean(arr2))
print("Median of arr2",np.median(arr2))
# print("mode",np.mode(arr1))

#Q8 Solve : x-2y+3z =9, -x+3y-z=-6 , 2x-5y+5z =17

arr1 = np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
arr2 = np.array([9,-6,17])
res = np.linalg.solve(arr1,arr2)
print("Result of x,y,z:",res)
arr1_inv = np.linalg.inv(arr1)
res = np.dot(arr1_inv,arr2)
print("Result using matrix inversion",res)

#Q9
import matplotlib.pyplot as plt

subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS']
sem1 = np.array([78, 85, 67, 90, 88])
sem2 = np.array([82, 80, 75, 92, 85])
x = np.arange(len(subjects))
plt.plot(x, sem1, label='Semester 1', color='blue', linestyle='--', marker='o')
plt.plot(x, sem2, label='Semester 2', color='red', linestyle='--', marker='s')
plt.title('Line Plot of Semester Results')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.xticks(x, subjects)
plt.legend()
plt.grid(True)
plt.show()




