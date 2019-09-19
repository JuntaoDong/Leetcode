class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n: # num1 shorter, num2 longer
            m, n = n, m
            nums1, nums2 = nums2, nums1
        min_idx = 0
        max_idx = m
        
        while min_idx <= max_idx:
            p1 = (min_idx + max_idx) >> 1
            p2 = (m + n + 1) // 2 - p1
            if p1 > 0 and p2 < n and nums1[p1 - 1] > nums2[p2]:
                max_idx = p1 - 1
            elif p1 < m and p2 > 0 and nums2[p2 - 1] > nums1[p1]:
                min_idx = p1 + 1
            else:
                if p1 == 0:
                    max_left = nums2[p2 - 1]
                elif p2 == 0:
                    max_left = nums1[p1 - 1]
                else:
                    max_left = max(nums1[p1 - 1], nums2[p2 - 1])
                if (m + n) % 2 == 1:
                    return max_left
                if p1 == m:
                    min_right = nums2[p2]
                elif p2 == n:
                    min_right = nums1[p1]
                else:
                    min_right = min(nums1[p1], nums2[p2])
                return (max_left + min_right) / 2
                    
        