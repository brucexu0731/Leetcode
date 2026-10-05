class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        #()() --> 1 + 1
        # (()()) --> 2 * 2 

        # (()(()()))

        #two stack, one keeping track of the open close pairs, the other one keeping track 
        #of the score thats waiting inside the open parenthesis to close 
        #[()]
        #[4]

        parens = []
        scores = []
        res = 0

        for i in range(len(s)):
            if s[i] == "(":
                parens.append(i)
                scores.append(0)
            else:
                parens.pop()
                score = 0
                if scores[-1] == 0:
                    score = 1
                else:
                    score = 2 * scores[-1]
                
                scores.pop()
                if not scores:
                    res += score
                else:
                    scores[-1] += score
        
        return res
                
        