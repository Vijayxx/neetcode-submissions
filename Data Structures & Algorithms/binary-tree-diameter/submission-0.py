# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getdia(node):
            if not node:
                return 0,0
            lh , ld= getdia(node.left)
            rh , rd= getdia(node.right)

            h = 1 + max(lh,rh)
            thisnode = lh + rh
            d = max(thisnode,rd,ld)

            return h,d
            
        return getdia(root)[1]
            