# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            dq = deque([root])
            depth = 0
            while dq:
                for _ in range(len(dq)):
                    ele = dq.popleft()
                    if ele.left:
                        dq.append(ele.left)
                    if ele.right:
                        dq.append(ele.right)
                depth += 1
            return depth
        if not root:
            return 0
        return bfs(root)