from collections import deque, defaultdict 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        indegrees = defaultdict(int)

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        
        queue = deque()
        res = []

        for n in range(numCourses):
            if indegrees[n] == 0:
                queue.append(n)
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                res.append(curr)

                for nxt in adj[curr]:
                    indegrees[nxt] -= 1
                    if indegrees[nxt] == 0:
                        queue.append(nxt)
        
        if len(res) != numCourses:
            return False
        else:
            return True


