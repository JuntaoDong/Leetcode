from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search has the least complexity of O(logN)
        l = 0
        r = len(nums)-1
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            while l <= r:
                m = (l + r)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            return l