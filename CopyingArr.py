from numpy import  *

num1 = array([1,2,4,6,9])
num2 = array([4,6,8,5,8])
num3 = num1+num2
print(num3)

print(sin(num1))
print(cos(num1))
print(sum(num1))

x = array([1,2,3,4,5])
y = x.view()
x[2] = 9
z = x.copy()
x[3] = 20
print(x)
print(y)
print(z)