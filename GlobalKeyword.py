
a = 10

def show():
    global a

    a = 20
  #  x = globals()['a']
    print(f'{a}  {id(a)}  in function')
    #print(f'{x}  {id(x)}  in function')

show()
print(f'{a}  {id(a)}  in outside function')