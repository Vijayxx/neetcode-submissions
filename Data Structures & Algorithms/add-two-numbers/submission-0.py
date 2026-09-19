# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1 = l1
        i2 = l2
        carry = 0
        su = ListNode()
        su1 = su
        while i1 or i2 or carry:
            summ = (i1.val if i1 else 0) + (i2.val if i2 else 0) + carry
            carry = summ // 10
            digit = summ % 10
            su1.next = ListNode(digit)
            su1 = su1.next
            if i1: i1 = i1.next
            if i2: i2 = i2.next
        return su.next

