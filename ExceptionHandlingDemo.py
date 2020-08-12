a = 5
b = 4

try:
    print('Resources Opened')
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Cannot be divid by zero")

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something is Wrong")

finally:
    print("Resources closed")