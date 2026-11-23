class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False
        else:
            for char in s:
                dict1[char] = dict1.get(char, 0) + 1
            for char in t:
                dict2[char] = dict2.get(char, 0) + 1

        if dict1 == dict2:
            return True
        return False
