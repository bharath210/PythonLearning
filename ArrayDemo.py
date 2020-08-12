from array import *

num1 = array('i',[3,8,7,5,8,6,4])

print(num1)
for i in range(len(num1)):
    print(num1[i])
print(num1.buffer_info())
num2 = array(num1.typecode,(a for a in num1))
num2.append(45)
for i in num2:
    print(i)