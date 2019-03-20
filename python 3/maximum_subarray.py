from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m, s = nums[0], nums[0]
        for num in nums[1:]:
            s = max(num, s+num)
            m = max(m, s)
        return m
                
            
