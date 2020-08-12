from numpy import  *

num1 = array([
                        [1,2,3,4,5,6],
                        [1,2,3,4,5,6]
                    ])

print(num1)
print(num1.dtype)
print(num1.ndim)
print(num1.shape)
print(num1.size)

num2 = num1.flatten()
print(num2)

num3 = num2.reshape(3,4)
print(num3)
print(num3.ndim)
num4 = num2.reshape(2,2,3)
print('after reshape')
print(num4)