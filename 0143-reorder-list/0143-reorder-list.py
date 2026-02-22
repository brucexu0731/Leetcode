# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head 
        
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        
        prev = slow
        curr = slow.next
        prev.next = None

        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt 

        curr = prev 
        curr2 = head 
    
        while curr.next:
            nxt2 = curr2.next 
            nxt = curr.next 
            curr2.next = curr
            curr.next = nxt2 
            curr2 = nxt2
            curr = nxt 
        



        