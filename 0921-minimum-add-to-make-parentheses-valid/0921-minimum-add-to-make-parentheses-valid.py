class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        
        return res + len(stack)