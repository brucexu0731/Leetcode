class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's 
        curr_sum = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            res = max(curr_sum, res)
        
        return res