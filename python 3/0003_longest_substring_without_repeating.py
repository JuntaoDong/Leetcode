class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        mapping = {}
        count = 0
        start = 0
        for i, l in enumerate(s):
            if l not in mapping:
                mapping[l] = i
                count += 1
            else:
                if mapping[l] < start:
                    mapping[l] = i
                    count += 1
                elif mapping[l] == start:
                    start += 1
                    mapping[l] = i
                else:
                    max_len = count if count > max_len else max_len
                    start = mapping[l] + 1
                    count = i - start + 1
                    mapping[l] = i
        max_len = count if count > max_len else max_len
        return max_len
