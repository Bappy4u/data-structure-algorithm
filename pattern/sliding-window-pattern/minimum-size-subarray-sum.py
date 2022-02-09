from typing import List

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                temp = nums[j:j+i+1]
                tempSum = sum(temp)
                if tempSum == target:
                    return i+1