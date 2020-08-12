a = int(input("How many drinks you want"))
avail = 5
i = 1
while a >= i:
    if i >= avail:
        print('out of stock')
        break

    print("Drink")
    i += 1

for i in range(1,31):
    if i % 5 == 0:
        continue
    print(i)

for i in range(1,31):
    if i % 2 !=0:
        pass
    else:
        print(i)