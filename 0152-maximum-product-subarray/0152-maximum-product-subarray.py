class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_max = nums[0]
        prev_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            curr_max = max(n, n * prev_max, n * prev_min)
            curr_min = min(n, n * prev_max, n * prev_min)
            res = max(res, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        
        return res


        