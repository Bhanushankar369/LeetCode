# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dq = deque([root])
        ind = 1

        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        while dq:
            level = []
            l = len(dq)
            for i in range(l):
                node = dq.popleft()
                level.append(node)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ind+=1
            if ind==depth:
                for i in range(len(level)):
                    tempLeft = level[i].left
                    tempRight = level[i].right

                    level[i].left = TreeNode(val)
                    level[i].right = TreeNode(val)

                    level[i].left.left = tempLeft
                    level[i].right.right = tempRight
        return root