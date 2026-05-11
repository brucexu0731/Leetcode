class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        
        # n = length 
        # array of k that can divide n, 1, 2, 3, 4, 6 ...
        # max number of k is about 120 given our range
        
        # for each k from 1 - n, we want to break down n to k subarrays, check if each subarray is
        # rotatable and sortable, then compare the max(s1) to min(s2)
        # to check if each subarray is rotatable, it means the array is already sorted and only rotated
        # go through each k 

        res = 0
        n = len(nums)

        for k in range(1, n + 1):
            if n % k:
                continue
            i = 0
            j = i + k
            sortable = True 
            max_prev = 0 
            min_curr = float('inf')

            while i < n:
                count = 0
                max_curr = nums[i]
                min_curr = nums[i]
                if k == 1:
                    max_curr = nums[i]
                    min_curr = nums[i]
                for x in range(i + 1, j):
                    if nums[x] < nums[x - 1]:
                        if nums[x] > min_curr:
                            sortable = False
                            break
                        count += 1
                    if nums[x] > max_curr and count > 0:
                        sortable = False
                        break

                    if count > 1:
                        sortable = False
                        break 
                    max_curr = max(max_curr, nums[x])
                    min_curr = min(min_curr, nums[x])
                if min_curr < max_prev:
                    sortable = False
                    break
                if nums[j - 1] > nums[i] and count > 0:
                    sortable = False
                    break
                max_prev = max_curr
                i = j
                j = i + k
            
            if sortable:
                res += k
        
        return res