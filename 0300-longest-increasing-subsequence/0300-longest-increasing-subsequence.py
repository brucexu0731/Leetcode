class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            longest = 0
            for j in range(i + 1, len(nums)):
                curr = dfs(j)
                if nums[j] > nums[i]:
                    longest = max(curr, longest)
            memo[i] = 1 + longest
            return 1 + longest 
        
        dfs(0)
            
        return max(memo.values())