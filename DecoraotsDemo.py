
def division(x,y):
    return  x/y

def smart_division(fun):
    def inner(a , b):
        if a < b :
            a,b = b,a
        return fun(a,b)
    return inner

division = smart_division(division)
print(division(5,10))