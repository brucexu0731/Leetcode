class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            longest = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    curr = dfs(j)
                    longest = max(curr, longest)
            memo[i] = 1 + longest
            return 1 + longest 
        
        res = 0
        for i in range(len(nums)):
            curr = dfs(i)
            res = max(curr, res)
            
        return res