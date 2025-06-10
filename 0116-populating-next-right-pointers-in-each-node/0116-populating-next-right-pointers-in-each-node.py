"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        ans = []
        dq = deque([root])
        while dq:
            l = len(dq)
            for i in range(l):
                ele = dq.popleft()
                if dq:
                    ele.next = dq[0]
                if ele.left:
                    dq.append(ele.left)
                if ele.right:
                    dq.append(ele.right)

            ele.next = None
        return root