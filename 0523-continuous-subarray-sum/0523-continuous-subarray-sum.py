class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    
    # good subarray --> length 2, sum of elements multiply of k 
    # the sum is multiple of k if sum % k == 0 

    # [23, 2, 4, 6, 7] --> 6 
    # [5, 2, 4, 0, 1] 
    # [-1, 2, 5, 6]  --> 4
    # [5, 1, 5, 4, 4, 2] --> 10 
    # [5, 6, 11, 15, 19, 21]
    # [5, 6, 1, 5, 9, 1]
    # [21, 16, 15, 10, 6, 2]
        if len(nums) < 2:
            return False
        tot = 0
        prefix = {0: -1}
        for i in range(len(nums)):
            n = nums[i]
            tot += n
            if tot % k in prefix and (i - prefix[tot % k] > 1):
                return True
            else:
                prefix[tot % k] = i if tot % k not in prefix else prefix[tot % k]
        
        return False
    #[23, 25, 29, 35, 41]
    #[2, 4, 1, 0, 6]
    #[1, 1]
    #[8, 14]
    #[1, 1, 1]