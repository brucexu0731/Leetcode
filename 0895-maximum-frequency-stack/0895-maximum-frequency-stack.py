
from collections import defaultdict
class FreqStack:

    def __init__(self):
        #a frequency map 
        self.freq = defaultdict(int)
        self.max_freq = 0
        self.freq_groups = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        if freq > self.max_freq:
            self.max_freq = freq
        self.freq_groups[freq].append(val)

    def pop(self) -> int:
        val = self.freq_groups[self.max_freq].pop()
        self.freq[val] -= 1
        while self.max_freq in self.freq_groups and not self.freq_groups[self.max_freq]:
            self.max_freq -= 1
        return val 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()