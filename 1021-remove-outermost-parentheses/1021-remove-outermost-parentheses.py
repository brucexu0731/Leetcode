class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        # so basically each primitive string is like the outter most brackets,
        # there are no other parenthesis closing it

        res = ""
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                l = stack.pop()
                if not stack:
                    res += s[l + 1 : i]
        
        return res
        