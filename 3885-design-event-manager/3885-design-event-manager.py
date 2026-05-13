import heapq
from collections import defaultdict
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.event = defaultdict(int)
        self.heap = []
        for event_id, priority in events:
            self.event[event_id] = priority
            heapq.heappush(self.heap, (-priority, event_id))

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, eventId))
        self.event[eventId] = newPriority

    def pollHighest(self) -> int:
        while self.heap and -self.heap[0][0] != self.event[self.heap[0][1]]:
            heapq.heappop(self.heap)
        if not self.heap:
            return -1
        priority, event = heapq.heappop(self.heap)
        self.event.pop(event)
        return event


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()