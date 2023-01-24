
import numpy as np

#creating array
x = np.array([22,33,44,55])
print(x)
#get the size of the array
print(x.size)
#get the shape & dimission
print(x.shape, x.ndim)

#can be create by using arange function
print(np.arange(10))
#---------------------------------------------------------

#creating 2dimissional array

d2_array = np.array([[1,2,3], [11,22,33], [111,222,333], [1111,2222,3333]])
# print(d2_array)
# print(d2_array.ndim)

#creating 2dimissional array by using arange & reshape functions
# arr2d = np.arange(20).reshape(1,20)
# arr2d = np.arange(20).reshape(20,1)
# arr2d = np.arange(20).reshape(4,5)
arr2d = np.arange(20).reshape(5,4)
# arr2d = np.arange(20).reshape(2,10)
# arr2d = np.arange(20).reshape(10,2)
print(arr2d)