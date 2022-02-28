from typing import List

def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2

        if arr[mid][0]>=val[1] and arr[mid]!=val:
            if arr[mid][0]==val[1]:
                return arr[mid]
            if arr[mid][0]>val[1]:
                mina = min(mina, arr[mid])
        # If x is greater, ignore left half
        if arr[mid][0] < val:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid][0] > val:
            high = mid - 1
 
        # means x is present at mid
    # If we reach here, then the element was not present
    return -1

def binarySearch(arr, val):
    l, r = 0, len(arr)-1
    mina = [pow(10,6) + 1, 0]
    while l<=r:
        mid = (r+l)//2
        if arr[mid][0]>=val[1] and arr[mid]!=val:
            if arr[mid][0]==val[1]:
                return arr[mid]
            if arr[mid][0]>val[1]:
                mina = min(mina, arr[mid])
        elif arr[mid][0]<val[1] and arr[mid] == val:
            l = mid + 1
        elif arr[mid][0]>val[1]:
            r = mid - 1


            
    if mina< [pow(10,6)+1, 0]:
        return mina
    
    return False
    

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = []
        sintervals = sorted(intervals)
        
        for i in intervals:
            ri = - 1
            temp = binarySearch(sintervals, i)
            if temp:
                ri = intervals.index(temp)
            
            arr.append(ri)
        return arr


sol = Solution()

sol.findRightInterval([[1,1],[3,4]])