class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        
        # n numbers, want their sum to be sum, and want to maximize their squared 
        # product

        # greedy: set them all as 1s, then try to get as many 9s as possible
        n = 0
        res = [0 for i in range(num)]
        if sum < 1 or sum > num * 9:
            return ""

        for i in range(len(res)):
            if sum < 9:
                res[i] += sum
                sum = 0
                break
            res[i] += 9
            sum -= 9
        
        res = [str(d) for d in res]
        
        return "".join(res)



        