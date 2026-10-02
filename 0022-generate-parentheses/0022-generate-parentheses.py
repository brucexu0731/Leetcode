class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        # explore all possibilities, backtrack if invalid, save valid 
        # outcomes in the end 

        # actually can just build valid outcomes recusively 

        res = []
        path = []

        def dfs(open, close):
            if open == 0:
                if close == 0:
                    combo = "".join(path)
                    res.append(combo)         
                elif close > 0:
                    path.append(")")
                    dfs(open, close - 1)
                    path.pop()
                return
            
            #so if there are same amount of open/closed parenthesis, we can only add open paren
            if open == close:
                path.append("(")
                dfs(open - 1, close)
            #if there are more opens than closed, the we can add either
            elif open < close:
                path.append("(")
                dfs(open - 1, close)
                path.pop()
                path.append(")")
                dfs(open, close - 1)
            
            path.pop()
        
        dfs(n, n)
        
        return res

            
            
