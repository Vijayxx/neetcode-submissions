# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        count = 0
        stack.append((root,root.val))
        while len(stack) > 0:
            node,maxsofar = stack.pop()
            if node:
                if node.val >= maxsofar:
                    count+=1
                    maxsofar = node.val
                stack.append((node.right,maxsofar))
                stack.append((node.left,maxsofar))
        return count

            


        
        
        