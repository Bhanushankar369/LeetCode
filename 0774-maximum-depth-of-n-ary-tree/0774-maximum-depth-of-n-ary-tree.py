"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def bfs(root):
            if not root:
                return []
            dq = deque([root])
            res = []
            while dq:
                level = []
                l = len(dq)
                for i in range(l):
                    ele = dq.popleft()
                    level.append(ele.val)
                    for child in ele.children:
                        dq.append(child)
                res.append(level)
            return res
        return len(bfs(root))