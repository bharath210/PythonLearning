
def sort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j] > nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp



val = [2,8,6,5,9,5,4,2]
val.sort()
print(val)
