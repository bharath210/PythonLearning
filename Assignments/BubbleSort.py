
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j+1] < nums[j]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp





val = [2,8,6,5,9,5,4,2]
val.sort()
print(val)