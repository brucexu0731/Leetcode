class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #so an island is not closed if it hits the edge of the board, otherwise it's closed
        # so just do flood fill and return true if every node can't reach water 
        row, col = len(grid), len(grid[0])
        visit = {}
        def dfs(r, c):
            if min(r, c) < 0 or r == row or c == col:
                return False
            if grid[r][c] == 1:
                return True
            if (r, c) in visit:
                return visit[(r, c)]
            
            visit[(r, c)] = True
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            visit[(r, c)] = up and down and left and right
            return visit[(r, c)]
        
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and (i, j) not in visit and dfs(i, j):
                    res += 1

        return res
            
