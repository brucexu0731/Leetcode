class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        stars = []
        

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False 
        
        while stack:
            if not stars or stars[-1] < stack[-1]:
                return False
            else:
                stack.pop()
                stars.pop()
        
        return True