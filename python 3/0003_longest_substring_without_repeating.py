class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        fast = 0
        max_len = 0
        mapping = set()
        while fast < len(s):
            if s[fast] not in mapping:
                mapping.add(s[fast])
                fast += 1
            else:
                slow += 1
                fast = slow
                max_len = len(mapping) if len(mapping) > max_len else max_len
                mapping.clear()
                mapping.add(s[fast])
                fast += 1
        max_len = len(mapping) if len(mapping) > max_len else max_len
        return max_len
