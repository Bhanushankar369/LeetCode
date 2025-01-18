# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0
        if not root:
            return None
        dq = deque([root])
        res = []
        while dq:
            ele = dq.popleft()
            if ele.left:
                dq.append(ele.left)
                if ele.val %2 == 0:
                    if ele.left.left:
                        total += ele.left.left.val
                    if ele.left.right:
                        total += ele.left.right.val
            if ele.right:
                dq.append(ele.right)
                if ele.val %2 == 0:
                    if ele.right.left:
                        total += ele.right.left.val
                    if ele.right.right:
                        total += ele.right.right.val
    
        return total