# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n +=1
        curr = head
        half = n//2
        prev = head
        while half > 1:
            prev = prev.next
            half -= 1
        
        second = prev.next
        prev.next = None
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        dummy = ListNode()
        tail = dummy
        l1 = head
        l2 = prev
        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        