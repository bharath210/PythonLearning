from _functools import *
nums = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda  n: n % 2 == 0,nums))
print(evens)
squers = list(map(lambda n: n*n,evens))
print(squers)
sum = reduce(lambda a,b: a + b,squers)
print(sum)