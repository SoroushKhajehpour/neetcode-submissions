class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            matching = target - num
            if matching in seen:
                return [seen[matching], index]
            seen[num] = index


    
