class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        ROW = len(matrix)
        COL = len(matrix[0])
        memo = {}
        def dfs(r, c):
            if c == COL or c < 0:
                return float('inf')
            if r == ROW - 1:
                return matrix[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = matrix[r][c] + min(dfs(r + 1, c - 1), dfs(r + 1, c), dfs(r + 1, c + 1))
            memo[(r, c)] = res

            return res
        
        res = float('inf')
        for i in range(COL):
            res = min(res, dfs(0, i))
        
        return res



            



        