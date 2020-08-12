from numpy import *

num1 = array([2.5,4,6.5,3,7],int)
print(num1)
print(num1.dtype)

num2 = linspace(1,20,5)
print(num2)

num3 = arange(1,20,2)
print(num3)

num4 = logspace(10,20,4)
print(num4)
print('%.2f' %num4[2])

num5 = zeros(4,int)
print(num5)

num6 = ones(5)
print(num6)