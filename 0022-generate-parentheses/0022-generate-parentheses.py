class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        # explore all possibilities, backtrack if invalid, save valid 
        # outcomes in the end 

        # actually can just build valid outcomes recusively 

        res = []

        def dfs(path, open, close):
            if open == 0:
                if close == 0:
                    res.append(path)         
                elif close > 0:
                    dfs(path + ")", open, close - 1)
                return
            
            #so if there are same amount of open/closed parenthesis, we can only add open paren
            if open == close:
                dfs(path + "(", open - 1, close)
            #if there are more opens than closed, the we can add either
            elif open < close:
                dfs(path + "(", open - 1, close)
                dfs(path + ")", open, close - 1)
        
        dfs("", n, n)
        
        return res

            
            
