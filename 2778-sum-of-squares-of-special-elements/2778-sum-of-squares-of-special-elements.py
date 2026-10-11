class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)

        for i in range(n):
            val = nums[i]
            if n % (i + 1) == 0:
                res += val ** 2 
        
        return res

        