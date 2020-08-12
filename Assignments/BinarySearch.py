
pos = -1
def search(list,n):
    l = 0
    u = len(list)-1
    global pos
    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            pos = mid
            return True
        else:
            if n > list[mid]:
                l = mid +1
            else:
                u = mid-1
    return  False

nums = [10,20,30,40,50,60,70,80]
n = 70

if search(nums,n):
    print('Fount at',pos+1)
else:
    print('Not Found')