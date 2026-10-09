class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        res = 0

        for i in range(len(s)):
            if s[i] == "(":
                if stack and stack[-1] == ")":
                    stack.pop()
                    stack.pop()

                stack.append("(")
                res += 2

            else:
                if not stack:
                    stack.append("(")
                    stack.append(")")
                    res += 2

                elif stack[-1] == "(":
                    res -= 1
                    stack.append(")")
                else:
                    res -= 1
                    stack.pop()
                    stack.pop()
        
        return res
        