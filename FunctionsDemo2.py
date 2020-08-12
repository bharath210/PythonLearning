def person(age,name):
    print(age)
    print(name)

person(25,'bharath')

person(name='vivek',age=18) #keywod args

def student(name, marks=35):  #default args
    print(name)
    print(marks)

student('Sansa')

# variable lenth args

def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)

sum(4,88,7,5,8)

def show(*a):
    for i in a:
        print(i)

show(32,'bharath',5.44)

# keyword variable lenth agrument

def employ(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

employ('bharath',id='E002',age=23,city='HYD',mob=9876543210)