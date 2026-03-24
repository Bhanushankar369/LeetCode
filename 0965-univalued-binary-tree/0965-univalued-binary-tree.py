# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val

        def traverse(root):
            if not root:
                return True
            if root.val != value:
                return False
            
            return traverse(root.left) and traverse(root.right)
        
        return traverse(root)