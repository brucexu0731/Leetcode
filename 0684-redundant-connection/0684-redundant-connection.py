from collections import defaultdict 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])
        
        visit = set()
        def dfs(n, path, prev):
            if n in visit:
                for i in range(len(path)):
                    if path[i] == n:
                        path = path[i:]
                        path.append(n)
                        break
                return path 


            visit.add(n)
            path.append(n)
            for v in adj_map[n]:
                if v == prev:
                    continue 
                cycle = dfs(v, path, n)
                if cycle:
                    return cycle 
            visit.remove(n)
            path.pop()
            return None

        cycle = dfs(edges[0][0], [], None)
        cycle_edges = set()
        for i in range(1, len(cycle)):
            cycle_edges.add((cycle[i - 1], cycle[i]))
            cycle_edges.add((cycle[i], cycle[i - 1]))
        
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            if (edge[0], edge[1]) in cycle_edges:
                return edge 




            