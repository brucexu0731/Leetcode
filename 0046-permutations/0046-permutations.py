class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path: List[int], nums):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                nums_copy = nums[:]
                path.append(nums[i])
                nums_copy.pop(i)
                dfs(path[:], nums_copy)
                path.pop()
        
        dfs([], nums)

        return res

