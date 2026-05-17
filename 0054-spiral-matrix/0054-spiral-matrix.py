class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visit = set()
        res = []
        row, col = len(matrix), len(matrix[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j, d):
            res.append(matrix[i][j])
            visit.add((i, j))
            dx, dy = direction[d]
            ni, nj = i + dx, j + dy

            if min(ni,nj) < 0 or ni == row or nj == col or (ni, nj) in visit:
                d = 0 if d == 3 else d + 1
                dx, dy = direction[d]
                ni, nj = i + dx, j + dy
                if min(ni,nj) < 0 or ni == row or nj == col or (ni, nj) in visit:
                    return 
                else:
                    dfs(ni, nj, d)
            else:
                dfs(ni, nj, d)
        
        dfs(0, 0, 0)

        return res



