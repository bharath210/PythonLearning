a = int(input("Enter a number"))

r = a % 2

if r == 0:
    print("It's an Even number")
else:
    print("It's an Odd number")


if a < 5:
    print('below 5')
elif a < 10:
    print('above 5 and below 10')
elif a < 20:
    print('above 10 and below 20')
else:
    print('above 20')