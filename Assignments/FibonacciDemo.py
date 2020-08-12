
def fibb(n):
    num1 = 0;
    num2 = 1;
    temp =0
    if(n == 1):
        print(num1)
    else:
        print(num1)
        print(num2)
        for i in range(2,n):
            num3 = num2 + num1
           # if n <= num3:
            #   break
            print(num3)
            temp = num3
            num1 = num2
            num2 = num3



x = int(input("Enter a number"))
fibb(x)