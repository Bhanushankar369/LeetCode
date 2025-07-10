"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        dq = deque([root])
        while dq:
            level = []
            for _ in range(len(dq)):
                ele = dq.popleft()
                level.append(ele)
                if ele.left:
                    dq.append(ele.left)
                if ele.right:
                    dq.append(ele.right)

            for i in range(1, len(level)):
                level[i-1].next = level[i]
            
            if level: level[-1].next = None
        return root