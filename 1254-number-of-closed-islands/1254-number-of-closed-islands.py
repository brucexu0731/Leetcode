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
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if not dfs(nr, nc):
                    visit[(r, c)] = False
                    return False
            return True 
        
        res = 0

        for i in range(row):
            for j in range(col):
                if (i, j) not in visit and grid[i][j] == 0:
                    if dfs(i, j):
                        res += 1

        return res
            
