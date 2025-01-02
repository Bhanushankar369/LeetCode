# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lst = []
        def inorder(root, lst):
            if root:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)
        inorder(root, lst)
        return sum(lst[lst.index(low) : lst.index(high)+1])