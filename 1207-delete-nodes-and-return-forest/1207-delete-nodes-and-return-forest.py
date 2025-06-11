# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorder(self, root, lst):
    #     if root:
    #         self.inorder(self, root.left, lst)
    #         lst.append(root.val)
    #         self.inorder(self, root.right, lst)

    # def justTravel(self, root, to_delete):
    #     if not root:
    #         return None
    #     if root.val in to_delete:
    #         root.val = -1
    #     self.justTravel(root.left, to_delete)
    #     self.justTravel(root.right, to_delete)

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        result = set([root])

        def dfs(node):
            if not node:
                return None

            res = node
            if node.val in to_delete:
                res = None
                result.discard(node)
                if node.left: result.add(node.left)
                if node.right: result.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res

        dfs(root)
        return list(result)