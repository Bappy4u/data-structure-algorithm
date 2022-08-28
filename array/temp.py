def zero(nums):
    r = len(nums)-1
    current = r
    while r>=0:
        if nums[r]!=0:
            nums[current] = nums[r]
            current -=1
        r -=1
    
    while current>=0:
        nums[current]=0
        current -=1


    return nums

print(zero([6,0,1,0,5]))