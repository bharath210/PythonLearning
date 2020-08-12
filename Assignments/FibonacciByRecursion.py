
def fib(n):
    if n<0:
        print('In Valid')

    elif n==1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

num = int(input('Enter a number'))


for i in range(1,num+1):
    res = fib(i)
    print(res,end=" ")