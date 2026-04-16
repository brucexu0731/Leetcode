class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        row,col = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if (r, c) in visit or min(r, c) < 0 or r == row or c == col or grid[r][c] == "0":
                return 
            
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visit and grid[r][c] != "0":
                    count += 1
                    dfs(r, c)
        
        return count
        