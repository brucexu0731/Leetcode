class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        
        def dfs(r, c):
            if min(r, c) < 0 or r == row or c == col:
                return False 
            
            if board[r][c] == 'X':
                return True
            
            if (r, c) in visit:
                return True
            
            visit.add((r, c))
            return dfs(r + 1, c) and dfs(r - 1, c) and dfs(r, c + 1) and dfs(r, c - 1)
        
        for r in range(row):
            for c in range(col):
                visit = set()
                if dfs(r, c):
                    for x, y in visit:
                        board[x][y] = 'X'
