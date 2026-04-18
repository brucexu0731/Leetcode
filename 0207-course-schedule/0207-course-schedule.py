from collections import defaultdict
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        visit = set()

        def dfs(n):
            if n in path:
                return False
            if n in visit:
                return True 

            res = True
            visit.add(n)
            path.add(n)
            for course in adj[n]:
                res &= dfs(course) 
            path.remove(n)
            return res 
        
        for i in range(numCourses):
            if i not in visit:
                path = set()
                if dfs(i) == False:
                    return False

        
        return True
        
