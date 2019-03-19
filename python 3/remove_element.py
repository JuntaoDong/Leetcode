from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0       # index
        k = 0       # counter
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            else:
                k += 1
        for i in range(k):
            nums.pop()
        return len(nums)
                
                
        