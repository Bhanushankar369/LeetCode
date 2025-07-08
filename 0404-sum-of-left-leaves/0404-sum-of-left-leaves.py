# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if not root:
                return 
            if not root.left and not root.right:
                if isLeft:
                    nonlocal total
                    total += root.val
                return

            dfs(root.left, True)
            dfs(root.right, False)

        total =0
        dfs(root, False)
        return total