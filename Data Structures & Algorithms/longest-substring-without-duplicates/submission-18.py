class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        max_length = 0

        for r in range(0, len(s)):
            if s[r] not in window:
                window.add(s[r])
            else:
                while s[r] in window:
                    window.remove(s[l])
                    l+=1
                window.add(s[r])
            if len(window) > max_length:
                max_length = len(window)
        return max_length

             

