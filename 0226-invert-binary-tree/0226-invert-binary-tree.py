# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return None
            dq = deque([root])
            while dq:
                level = []
                l = len(dq)
                for _ in range(l):
                    ele = dq.popleft()
                    level.append(ele)
                    if ele.left:
                        dq.append(ele.left)
                    if ele.right:
                        dq.append(ele.right)

                for node in level:
                    temp = node.left
                    node.left = node.right
                    node.right = temp
        bfs(root)
        return root
