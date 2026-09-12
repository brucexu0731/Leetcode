class DynamicUnionFind:

    def __init__(self):
        self.root = {}
        self.rank = {}
    
    def add(self, r, c):
        self.root[(r, c)] = (r, c) 
        self.rank[(r, c)] = 1
    
    def find(self, r, c):
        if self.root[(r, c)] != (r, c):
            nr, nc = self.root[(r, c)]
            self.root[(r, c)] = self.find(nr, nc)
        return self.root[(r, c)]
    
    def union(self, r1, c1, r2, c2):

        root1 = self.find(r1, c1)
        root2 = self.find(r2, c2)

        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.root[root1] = root2
        else:
            self.root[root2] = root1
            self.rank[root1] += 1
        
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        UF = DynamicUnionFind()
        grid = [[0] * n for i in range(m)]
        curr = 0
        res = []

        for r, c in positions:
            if grid[r][c] == 1:
                res.append(curr)
                continue

            grid[r][c] = 1
            UF.add(r, c)
            curr += 1

            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if min(nr, nc) < 0 or nr == m or nc == n or grid[nr][nc] == 0:
                    continue

                if UF.union(r, c, nr, nc):
                    curr -= 1 
            
            res.append(curr)
        
        return res




