# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        curr = 0
        def dfs(root, curr):
            if not root:
                return 

            if not root.left and not root.right:
                nonlocal ans
                ans += curr
                return 

            if root.left:
                dfs(root.left, curr*10 + root.left.val)
            if root.right:
                dfs(root.right, curr*10 + root.right.val)
        
        dfs(root, curr*10 + root.val)
        return ans