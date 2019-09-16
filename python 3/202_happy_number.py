class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        d = {}
        while s is not 1:
            s = 0
            for i in range(len(str(n))):
                s += int(str(n)[i])**2
            if s not in d:
                d[s] = 1
            else:
                return False
            n = s
        return True
