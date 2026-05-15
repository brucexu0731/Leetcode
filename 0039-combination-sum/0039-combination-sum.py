class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []
        def dfs(i, curr_sum):
            if i == len(candidates) or curr_sum > target:
                return
            if curr_sum == target:
                res.append(path[:])
                return
            
            dfs(i + 1, curr_sum)

            n = candidates[i]
            path.append(n)
            dfs(i, curr_sum + n)
            path.pop()
        
        dfs(0, 0)
        return res