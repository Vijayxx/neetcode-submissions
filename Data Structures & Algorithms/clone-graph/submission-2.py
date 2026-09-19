"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        d = {}
        seen = set()
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in seen:
                d[curr] = Node(curr.val)
                seen.add(curr)
                for i in curr.neighbors:
                    stack.append(i)
        print(d)

        curr = node

        for curr in d:
            for i in curr.neighbors:
                d[curr].neighbors.append(d[i])

        
        return d[node]
            
            