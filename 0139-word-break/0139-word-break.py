class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # leetcode: l -> le -> lee -> check dictionary for match while addinge each char
        # if match -> we do dfs on the rest of the string otherwise-> keep going 
        # worst case time complexity we have len(s) recursive steps, and at each step we have
        # len(s) cases 
        # dp with memoization 
        words = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            j = i + 1
            res = False
            while j <= len(s) and not res:
                if s[i : j] in words:
                    res = dfs(j)
                j += 1
            memo[i] = res
            return res 

        return dfs(0)
            
