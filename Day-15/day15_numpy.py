import numpy as np

#task-1 Indexing practice
arr=np.arange(1,11)
print("first element:", arr[0])
print("middle element:",arr[5])
print("last element:", arr[-1])

arr2=np.arange(1,17).reshape(4,4)
print(arr2)
print("first row:", arr2[0])
print("last row", arr2[-1])
print("first column:",arr2[:,0])
print("last column:", arr2[:,-1])

arr3=np.arange(1,25).reshape(2,3,4)
print(arr3)
print("element:", arr3[0,1,2])
print("element:", arr3[1,2,3])


#Task-2  Indexing Practice
matrix=np.arange(1,26).reshape(5,5)
print(matrix)
print("First row:", matrix[0])
print("last row", matrix[-1])
print("first column", matrix[:,0])
print("last column", matrix[:,-1])
print("3*3 submatrix", matrix[1:4,1:4])
print("reverse row", matrix[::-1])
print("reverse columns", matrix[:,::-1])


#task-3 Reshaping
mat=np.arange(1,13)
a=mat.reshape(3,4)
b=mat.reshape(2,6)
c=mat.reshape(4,3)
print("3*4 matrix:", a)
print("2*6 matrix:", b)
print("4*3 matrix:", c)
print("flatten:", a.flatten())
print("flatten:", b.flatten())
print("flatten:",c.flatten())
print("Transpose of 3*4:", a.T)
