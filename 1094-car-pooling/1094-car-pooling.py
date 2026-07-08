from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        #sweepline
        events = defaultdict(int)

        for n, s, e in trips:
            events[s] += n
            events[e] -= n
        
        riders = 0
        for i in sorted(events.keys()):
            riders += events[i]
            if riders > capacity:
                return False
        
        return True

