
def fact(n):
    x =1
    for i in range(1,n+1):
        x = x * i
    return x

num = int(input('Enter a number'))
res = fact(num)
print(res)