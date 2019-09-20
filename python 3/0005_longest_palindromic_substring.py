# method1 - use common longest substring and check indices
class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = ''.join(reversed(s))
        cache = [[0 for i in range(len(s))] for j in range(len(r))]
        out = ''
        # column name: s;  row name: r
        for i in range(len(r)):  # r
            for j in range(len(s)):
                if r[i] == s[j]:
                    if i == 0 or j == 0:
                        cache[i][j] = 1
                    else:
                        cache[i][j] = cache[i-1][j-1] + 1
                    if cache[i][j] >= len(out) and j == len(s) - 1 - (i - cache[i][j] + 1):
                        out = s[j - cache[i][j] + 1:j + 1]
        return out


# method2 - use dynamic programming
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        cache = [[None for i in range(l)] for j in range(l)]
        out = ''
        for x in range(l):
            cache[x][x] = True
            out = s[x] if len(out) < 1 else out
            if x < l - 1:
                if s[x] == s[x+1]:
                    cache[x][x+1] = True
                    out = s[x:x+2] if len(out) < 2 else out
                else:
                    cache[x][x+1] = False
        for i in range(l-3, -1, -1):
            for j in range(i+2, l):
                if (cache[i+1][j-1] == True) and (s[i] == s[j]):
                    cache[i][j] = True
                    if j - i + 1 >= len(out):
                        out = s[i:j+1]

        return out

# method3 - start from middle
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        out = ''
        for i in range(l):
            out = max(self.helper(s, i, i), self.helper(
                s, i, i+1), out, key=len)
        return out

    def helper(self, s, start, end):
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break
        return s[start+1:end]
