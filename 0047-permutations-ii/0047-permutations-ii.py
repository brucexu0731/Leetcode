class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        #is the array sorted? 
        def dfs(path: List[int], nums):
            if not nums:
                res.append(path)
            unique = set()
            for i in range(len(nums)):
                if nums[i] in unique:
                    continue
                unique.add(nums[i])
                path.append(nums[i])
                nums_copy = nums[:]
                nums_copy.pop(i)
                dfs(path[:], nums_copy)
                path.pop()
        
        dfs([], nums)
        return res