class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0
        group = []

        for R in range(len(nums)):
            if nums[R] not in group:
                group = []
            group.append(nums[R])

            if R < 2:
                nums[L] = nums[R]
                L += 1
                continue
            
            if len(group) > 2:
                continue 
            else:
                nums[L] = nums[R]
                L += 1
        
        return L



