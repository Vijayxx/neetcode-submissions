"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        d = {}
        curr1 = Node(0)
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        print(d)
        curr = head
        while curr:
            d[curr].next = d.get(curr.next)
            d[curr].random = d.get(curr.random)
            curr = curr.next
        return d[head]

