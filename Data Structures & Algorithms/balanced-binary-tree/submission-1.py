# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0,True
            
            lh,lt = check(node.left)
            if not lt:
                return 0,False
            rh,rt = check(node.right)
            if not rt:
                return 0,False

            return 1+max(lh,rh),True if abs(lh - rh) <= 1 else False
        
        return check(root)[1]
        