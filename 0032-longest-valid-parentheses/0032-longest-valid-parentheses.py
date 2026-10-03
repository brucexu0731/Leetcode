class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        #brute force: explore every substring --> n^2 
        #sliding window --> doesn't work 

        #shrinking window  

        stack = []
        res = 0
        prev = -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            
            if s[i] == ')':
                if stack:
                    stack.pop()

                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        res = max(res, i - prev)
                else:
                    prev = i
        
        return res
        