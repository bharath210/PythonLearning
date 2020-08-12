nums = []

n = int(input("number of values"))

for i in range(n):
    val = int(input('enter value'))
    nums.append(val)

def evenOddCount(vals):
    even = 0
    odd = 0
    for i in vals:
        if(i % 2 == 0):
            even += 1
        else:
            odd += 1
    return even,odd

even,odd = evenOddCount(nums)
print("Even : {} Odd : {} ".format(even,odd))