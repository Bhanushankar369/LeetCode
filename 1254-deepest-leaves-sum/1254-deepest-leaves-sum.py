# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return None
            dq = deque([root])
            res = []
            while dq:
                level = []
                l = len(dq)
                for i in range(l):
                    ele = dq.popleft()
                    level.append(ele.val)
                    if ele.left:
                        dq.append(ele.left)
                    if ele.right:
                        dq.append(ele.right)
                res.append(level)
            return sum(res[-1])
        return bfs(root)