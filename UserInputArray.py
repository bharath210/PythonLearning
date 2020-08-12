from array import *

num = array('i')

n = int(input('enter the size of array'))
for i in range(n):
    x = int(input(f'Enter the value - {i+1}'))
    num.append(x)
print(num)
val = int(input('Enter the value'))

for j in range(len(num)):
    if val == num[j]:
        print(j)
        break

print(num.index(val))