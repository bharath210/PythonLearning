
x = [32,34,15,36,32,22]

for i in x:
    if i % 5 == 0:
        print(i)
        break
else:
    print('Not Found')