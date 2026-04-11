class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(path, i):
            if i >= len(nums):
                res.append(path[:])
                return 
            
            path.append(nums[i])
            dfs(path[:], i + 1)
            path.pop()
            dfs(path[:], i + 1)
        
        dfs([], 0)
        return res