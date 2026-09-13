from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visit = set()

        def dfs(n, path):
            if n in path:
                return False 
            if n in visit:
                return True
            
            path.add(n)
            visit.add(n)

            for nxt in adj[n]:
                if not dfs(nxt, path):
                    return False 
            
            path.remove(n)
            return True
        
        for n in range(numCourses):
            if not dfs(n, set()):
                return False
        
        return True