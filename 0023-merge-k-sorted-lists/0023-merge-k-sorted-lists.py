# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy_head = ListNode(-1)
        curr = dummy_head
        min_heap = []

        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(min_heap, (node.val, i, node))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next 

            if not node.next:
                continue
            else:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy_head.next
                

