import heapq
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # a min heap to keep track of all the end times of meeting rooms, keeping track of the room number
        # a min heap to keep track of all the available rooms

        # each round, get smallest of all the available rooms for the meeting, push it into
        # the first heap
        # if no rooms are available, pop all the rooms that finish before the start time, push them all back to the second heap and get the top one
        # if no rooms are available and all meetings are still ongoing, wait for the first room to finish
        # we have m meetings, each meeting is on average 3 operations: pop from available, push
        # into busy, pop from busy
        # so runtime is m log(n) + m log(m) to sort start times 
        meetings.sort()

        available = [i for i in range(n)]
        heapq.heapify(available)
        busy = []
        usage = defaultdict(int)
        for s, e in meetings:
            while busy and busy[0][0] <= s:
                end, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            if available:
                room = heapq.heappop(available)
                usage[room] += 1
                heapq.heappush(busy, [e, room])
            else:
                end, room = heapq.heappop(busy)
                usage[room] += 1
                heapq.heappush(busy, [end + e - s, room])

        #print(usage)
        max_usage = 0
        max_room = 0
        for room, count in usage.items():
            if count == max_usage:
                max_room = min(max_room, room)
            if count > max_usage:
                max_usage = count
                max_room = room
        return max_room


