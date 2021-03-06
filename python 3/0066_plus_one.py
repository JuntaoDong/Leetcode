from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while i >= -len(digits):
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)

        return digits