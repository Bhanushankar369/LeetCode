# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        dq = deque()
        def bfs(root):
            dq = deque([root])
            while dq:
                l = len(dq)
                level = []
                for i in range(l):
                    new = dq.popleft()
                    level.append(new)
                    if new.left:
                        dq.append(new.left)
                    if new.right:
                        dq.append(new.right)

                res.append(level[-1].val)
        bfs(root)
        return res
                