class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        i = 0
        while s[i] == ' ':
            i += 1
            if i == len(s):
                return 0
        if s[i] in '-+':
            j = i + 1
            while j < len(s) and s[j] in '0123456789':
                j += 1
            if j == i + 1:
                return 0
            num = int(s[i:j])
            if num < - 2 ** 31:
                return - 2 ** 31
            elif num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return num
        elif s[i] in '0123456789':
            j = i + 1
            while j < len(s) and s[j] in '0123456789':
                j += 1
            num = int(s[i:j])
            if num < - 2 ** 31:
                return - 2 ** 31
            elif num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return num
        else:
            return 0
