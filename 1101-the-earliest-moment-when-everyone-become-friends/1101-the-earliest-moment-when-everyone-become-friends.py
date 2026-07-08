class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.rank = {}
        for i in range(n):
            self.root[i] = i
            self.rank[i] = 0
    
    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        #print(p1, p2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.root[p2] = p1
        elif self.rank[p1] == self.rank[p2]:
            self.root[p2] = p1
            self.rank[p1] += 1
        else:
            self.root[p1] = p2
        
        return True


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)

        for t, p1, p2 in logs:
            if uf.union(p1, p2):
                n -= 1
                if n == 1:
                    return t
        
        return -1
            
        