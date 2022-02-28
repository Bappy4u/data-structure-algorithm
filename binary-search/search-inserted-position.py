class Solution(object):
    def searchInsert(self, nums, target):
        for i, val in enumerate(nums):
            if val >= target:
                return i
            
        return i+1
            