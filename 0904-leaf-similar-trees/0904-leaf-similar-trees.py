# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root, lst):
            if not root:
                return
            if not root.left and not root.right:
                lst.append(root.val)
                return
            traverse(root.left, lst)
            traverse(root.right, lst)

        lst1 = []
        lst2 = []
        traverse(root1, lst1)
        traverse(root2, lst2)
        return lst1 == lst2