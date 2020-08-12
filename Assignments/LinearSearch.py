pos = -1
def search(list,n):
    for i in list:
        global pos
        pos += 1
        if i == n:

            return True

    return False

nums = [10,2,3,4,5,6]
n = 4

if search(nums,n):
    print('Found at',pos+1)
else:
    print('Not Found')