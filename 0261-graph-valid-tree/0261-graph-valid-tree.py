from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree means no cycles, 1 connected component
        # Union find 
        # topo sort DFS 

        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visit = set()
        
        def dfs(n, prev):
            visit.add(n)
            res = True 
            for node in adj[n]:
                if node == prev:
                    continue
                if node in visit:
                    return False
                else:
                    res = res and dfs(node, n)
            return res

        res = dfs(0, 0)
        return res and len(visit) == n