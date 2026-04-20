from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visit = set()
        res = []

        def dfs(course, path):
            if course in path:
                return False
            if course in visit:
                return True 
            
            path.add(course)

            for pre in adj[course]:
                if not dfs(pre, path):
                    return False
            
            visit.add(course)
            res.append(course)
            path.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return []
        
        return res
