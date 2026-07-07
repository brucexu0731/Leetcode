from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # contruct a graph out of this, then for each island we would need to take the 
        # classes sequentially, which means we just need to compute the longest paths from
        # root to leaf in each island

        #courses are from 1 to n
        adj = defaultdict(list)
        for prev, nxt in relations:
            adj[prev].append(nxt)
        #possible to complete every course, so no cycles

        #do dfs on every path, memoize the longest dist to leaf
        memo = {}
        res = 0
        def dfs(i):
            nonlocal res 
            if i in memo:
                return memo[i]

            curr = 0
            for nxt in adj[i]:
                curr = max(curr, dfs(nxt))
            curr += time[i - 1]
            memo[i] = curr
            res = max(res, curr)
            return curr
            
        for i in range(1, n + 1):
            dfs(i)
        return res

            
