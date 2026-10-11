class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(len(nums)):
            n = nums[i]
            if len(nums)% (i + 1) == 0:
                res += n**2 
        
        return res

        