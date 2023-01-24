
import numpy as np

#creating array
x = np.array([22,33,44,55])
# print(x)
#get the size of the array
# print(x.size)
#get the shape & dimission
# print(x.shape, x.ndim)

#can be create by using arange function
# print(np.arange(10))
#---------------------------------------------------------

#creating 2dimissional array

d2_array = np.array([[1,2,3], [11,22,33], [111,222,333], [1111,2222,3333]])
# print(d2_array)
# print(d2_array.ndim)

#creating 2dimissional array by using arange & reshape functions
# arr2d = np.arange(20).reshape(1,20)
# arr2d = np.arange(20).reshape(20,1)
# arr2d = np.arange(20).reshape(4,5)
# arr2d = np.arange(20).reshape(5,4)
# arr2d = np.arange(20).reshape(2,10)
# arr2d = np.arange(20).reshape(10,2)
# print(arr2d)

#--------------------------------------------------------------------

#creating 3dmissional array

arr3d = np.arange(64).reshape(4,4,4)
# print(arr3d)

#vactorlized operations --> mulitplying 3d array with 2 and all the elements will multiplied by 2
# print(arr3d*2)

#Additions of two arrays

x1 = np.arange(4)
y1 = np.arange(4)
print(x1)
print(y1)
print(x1+y1)

#mirroring or element operations
m1 = np.arange(25).reshape(5,5)
m2 = np.arange(25,50).reshape(5,5)
# print(f"m1: {m1} and \n m2: {m2} \n ")
# print(f"{m1 + m2}\n")
#mulitplication with linear algebra
print("Linear Algebra mulitplication")
# print(m1@m2)

#mask
# print(m1)
# print(m1 > 5)
# print(m1[m1>10])

#build in where function
# print(np.where(m1>10, 0, m1))
# print(m1[(m1%2==0) & (m1%7==0)])
# print(np.where((m1%2==0) | (m1%7==0)))
print(np.where((m1%2==0) | (m1%7==0), "woo", "oho"))


