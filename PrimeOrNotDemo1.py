num = int(input("Enter a number"))
temp = (num+2)//2

for i in range(2,temp):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print('Prime')