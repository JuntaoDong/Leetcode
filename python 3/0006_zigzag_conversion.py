class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        result = []
        interval = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), interval):
                result.append(s[j])
                if i > 0 and i < numRows-1 and j+interval-2 * i < len(s):
                    result.append(s[j+interval-2*i])
        return ''.join(result)
