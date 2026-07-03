class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        row, col = len(matrix), len(matrix[0])
        def dfs(i, j, prev):
            if min(i, j) < 0 or i == row or j == col or prev >= matrix[i][j]:
                return 0 
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                res = max(res, dfs(ni, nj, matrix[i][j]))
            
            res += 1
            memo[(i, j)] = res
            return res
        
        res = 1
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c, -1))
        
        return res
            