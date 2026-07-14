import numpy as np

#task1 
#1D array
arr1=np.array([10,20,30,40])

#2D array
arr2=np.array([[1,2,3],[4,5,6]])

#3D array
arr3=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
    ])

#zeroes
zeroes=np.zeros((2,3))

#Ones 
ones=np.ones((3,4))

#arange
arange_arr=np.arange(1,11)

#linespace
linespace_arr=np.linspace(0,100,5)

print("1d array", arr1)
print("2d array", arr2)
print("3d array", arr3)
print("zeroes array", zeroes)
print("ones array", ones)
print("arange array", arange_arr)
print("linespace array", linespace_arr)


#task 2

import numpy as np

arrays = {
    "1D": np.array([10,20,30]),
    "2D": np.array([[1,2],[3,4]]),
    "3D": np.array([[[1,2],[3,4]],[[5,6],[7,8]]]),
    "Zeros": np.zeros((2,2)),
    "Ones": np.ones((3,3))
}

for name, arr in arrays.items():
    print("\n", name)
    print(arr)
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Data Type:", arr.dtype)

#task-3

#create numbers from 1 to 20
serial=np.arange(1,21)
print (serial)

#create 10 evenly spaced numbers between 0 and 100
even=np.arange(0,100,10)
print (even)

#create a 3*3 matrix of ones
mat=np.ones((3,3))
print(mat)

#create a 2*4 matrix from nested python list
mat2=np.array([
    [1,2,3,4],
    [5,6,7,8]
])



