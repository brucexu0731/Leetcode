class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        
        # decrement the largest difference by 1 each time 
        # use binary search to find the lowest max difference we can get 

        #1, 4, 10, 12   5, 8, 6, 9 ==> 4, 4, 4, 3. k1+k2 = 2

        # so for a lower boundary binary search, we would go left < right and left/right = mid because mid can be the answer, while exact value searches we do left <= right and left/right = mid +- 1 because we are looking for exact values

        diff = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        print(diff)
        operations = k1 + k2
        l, r = 0, max(diff)

        while l < r:
            m = (l + r) // 2

            moves = 0
            for n in diff:
                if n > m:
                    moves += n - m
            #m is too small
            if moves > operations:
                l = m + 1
            #m is too large
            elif moves <= operations:
                r = m
        
        moves = 0
        level = l
        for n in diff:
            if n > level:
                moves += n - level
        operations -= moves
        res = 0 

        print(level, operations)

        for n in diff:
            if n >= level:
                n = level
                if operations > 0:
                    operations -= 1
                    n -= 1
            res += max(n, 0) ** 2
            print(res)

        return res

