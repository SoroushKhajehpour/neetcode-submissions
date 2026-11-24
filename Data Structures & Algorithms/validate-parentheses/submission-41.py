class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        pairs = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if len(stack) == 0 or char != pairs[stack[-1]]:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        return False
      

        
        