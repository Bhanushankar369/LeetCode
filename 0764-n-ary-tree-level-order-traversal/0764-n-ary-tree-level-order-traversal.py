"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        dq = deque([root])
        res = []
        while dq:
            level=[]
            l = len(dq)
            for i in range(l):
                ele = dq.popleft()
                level.append(ele.val)
                for child in ele.children:
                    dq.append(child)
            res.append(level)
        return res