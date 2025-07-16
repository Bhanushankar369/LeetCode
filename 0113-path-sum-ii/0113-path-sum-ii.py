# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, level, total):
            if not root:
                return 

            total += root.val
            level.append(root.val)
            
            if not root.left and not root.right:
                if total == targetSum:
                    result.append(level[:])

            dfs(root.left, level, total)
            dfs(root.right, level, total)

            level.pop()


        dfs(root,[], 0)
        return result