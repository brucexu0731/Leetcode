import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = []

        for i, n in enumerate(nums):
            heapq.heappush(min_heap, (n, i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0][0]

