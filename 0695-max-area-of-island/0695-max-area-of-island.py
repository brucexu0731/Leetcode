class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        largest = 0
        
        def fill(r, c):
            count = 1
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0

            visit.add((r, c))
            count += fill(r + 1, c) 
            count += fill(r - 1, c) 
            count += fill(r, c + 1) 
            count += fill(r, c - 1) 

            return count
            
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visit and grid[i][j] != 0:
                    area = fill(i, j)
                    largest = max(largest, area)

        return largest