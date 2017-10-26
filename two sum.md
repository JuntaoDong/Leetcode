Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution 1: Brute force

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]      
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
Time complexity: O(n^2) 
Space complexity: O(1)
Run time: 26ms

Solution 2: by using dictionary(hash table)

class Solution(object):
    def twoSum(self, nums, target):
        dic = {v:k for k, v in enumerate(nums)}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in nums and nums.index(c)!=i:
                return [i, nums.index(c)]
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
Time complexity: O(n) 
Space complexity: O(n)
Run time: 33ms        
