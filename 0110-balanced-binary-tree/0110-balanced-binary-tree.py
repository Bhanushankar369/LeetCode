# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def maxDepth(root):
            if not root:
                return 0

            left = maxDepth(root.left)
            right = maxDepth(root.right)

            return max(left, right)+1

        dq = deque([root])

        while dq:
            for i in range(len(dq)):
                left = 0
                right = 0
                ele = dq.popleft()
                if ele.left:
                    left = maxDepth(ele.left)
                    dq.append(ele.left)
                if ele.right:
                    right = maxDepth(ele.right)
                    dq.append(ele.right)

                if not -1 <= left-right <= 1:
                    return False
        
        return True