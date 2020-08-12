
f1 = open('Demo.txt','r')

#print(f1.read())
#print(f1.readline(),end='')
#for data in f1:
#    print(data,end='')

f2 = open('Demo1.txt','w')
#f2.write("Hi Bharath")

#f3 = open('Demo1.txt','a')

for data in f1:
    f2.write(data)

