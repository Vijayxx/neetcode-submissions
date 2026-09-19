# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        
        if l == n:
            return head.next
        n = l - n
        prev = head
        while n > 1:
            prev = prev.next
            n -= 1
        
        prev.next = prev.next.next

        return head

