class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])

        res = 0
        visit = {}
        def dfs(r, c):
            nonlocal count
            if min(r, c) < 0 or r == row or c == col:
                return False
            if grid[r][c] == 0:
                return True
            if (r, c) in visit:
                return visit[(r, c)]
            
            visit[(r, c)] = True
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            res = up and down and left and right

            visit[(r, c)] = res
            count += 1
            return res
        
        for i in range(row):
            for j in range(col):
                count = 0
                if grid[i][j] == 1 and (i, j) not in visit and dfs(i, j):
                    res += count
        
        return res