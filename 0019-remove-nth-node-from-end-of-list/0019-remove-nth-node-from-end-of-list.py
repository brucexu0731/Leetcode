# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next 
        
        l = length - n 

        if l == 0:
            return head.next 
        
        curr2 = head
        for i in range(l - 1):
            curr2 = curr2.next 
        curr2.next = curr2.next.next

        return head
            


        