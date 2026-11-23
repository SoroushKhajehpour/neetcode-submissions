class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matching = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in matching:
                matching[sorted_string].append(string)
            else: 
                matching[sorted_string] = [string]

        return list(matching.values())
        