class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        new = 0
        while x > 0:
            x, digit = divmod(x, 10)
            new = new * 10 + digit 
            if new >= 2**31-1: 
                return 0
        return new if is_negative is False else -new
