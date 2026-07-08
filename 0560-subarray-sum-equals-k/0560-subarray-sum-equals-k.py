from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #hashmap + prefix sums
        # compute prefix sums and store value in hashmap as we are computing,
        # at every index check if curr_sum - k is in hashmap

        sums = defaultdict(int)
        sums[0] += 1
        prefix = 0
        res = 0

        for n in nums:
            prefix += n
            sums[prefix] += 1
            if prefix - k in sums:
                if k == 0:
                    res += sums[prefix - k] - 1
                else:
                    res += sums[prefix - k]
        
        return res

