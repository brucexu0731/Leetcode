class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """

        #sorted by start time
        #can maximize number of tasks if I sort by end time 

        #dp 

        intervals = []
        for i in range(len(startTime)):
            intervals.append([startTime[i], endTime[i], profit[i]])
        
        intervals.sort(key = lambda x: [x[0], -x[1], x[2]])
        #print(intervals)

        res = 0
        memo = {}

        #iteratively explore every valid combination of schedules
        #cache the max profit that each task can hold with its remaining tasks --> 

        def dfs(i):

            if i in memo:
                return memo[i]
            if i >= len(intervals):
                return 0

            start, end, prof = intervals[i]
            
            skip = dfs(i + 1)

            #binary search for most recent valid start

            l, r = i + 1, len(intervals) - 1

            while l <= r:
                m = (l + r) // 2
                s = intervals[m][0]
                
                if s < end:
                    l = m + 1
                elif s >= end:
                    r = m - 1
            
            keep = dfs(l) + prof

            memo[i] = max(skip, keep)
            return memo[i]

        return dfs(0)


            


        
        return res
            
            



        