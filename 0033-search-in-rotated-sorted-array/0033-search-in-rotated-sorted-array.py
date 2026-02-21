class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # when mid point is in left sorted array (if nums[m] is equal to nums[l] it is in the left sorted) 
            if nums[m] >= nums[l]:
                #if target is greater than mid point, we cam only seach right
                if target > nums[m]:
                    l = m + 1
                #if target is less than mid point, it's either in the left sorted array or it wrapped around
                else:
                    #checking if in left sorted array
                    if target >= nums[l]:
                        r = m - 1
                    #it's in right sorted array
                    else:
                        l = m + 1
            
            #when mid point is in the right sorted array
            elif nums[m] < nums[l]:
                # if target is smaller than m we can only search left 
                if target < nums[m]:
                    r = m - 1
                # if target is larget than m it's either in the right sorted array or it wrapped around
                else:
                    #check if in right sorted array
                    if target <= nums[r]:
                        l = m + 1
                    #it's in left sorted array
                    else:
                        r = m - 1


        return -1