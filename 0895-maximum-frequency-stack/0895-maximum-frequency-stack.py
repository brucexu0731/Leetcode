import heapq
from collections import defaultdict
class FreqStack:

    def __init__(self):
        #a frequency map 
        self.heap = []
        self.counter = 0
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.heap, (-self.freq[val], -self.counter, val))
        self.counter += 1

    def pop(self) -> int:
        curr = heapq.heappop(self.heap)
        val = curr[2]
        self.freq[val] -= 1
        return val 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()