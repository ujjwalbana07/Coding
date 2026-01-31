# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0 
        curr = head 
        while curr!=None:
            l = l+1
            curr = curr.next
        curr = head
        if n == l:
            return head.next
        for i in range(l- n -1):
            curr = curr.next
        
        curr.next = curr.next.next 

        curr = head 

        return curr
        