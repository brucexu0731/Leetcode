"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #sort everything, and the just do 2 pointers on the sorted list of intervals

        intervals = []
        for person in schedule:
            for i in person:
                intervals.append([i.start, i.end])
        
        intervals.sort()
        #print(intervals)
        
        res = []
        s = intervals[0][1]
        e = intervals[0][1]

        for start, end in intervals:
            if s < start:
                e = start
                res.append(Interval(s, e))
                s = end
            else:
                s = max(s, end)
        
        return res

