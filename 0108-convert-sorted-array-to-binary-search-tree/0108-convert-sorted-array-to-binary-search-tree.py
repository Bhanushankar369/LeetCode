# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    # def insertt(self, root, key):
        # temp = TreeNode()
        # temp.val = key
        # if root == None:
        #     temp.right = None
        #     temp.left = None
        #     root = temp
        # return temp
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        
        # root = TreeNode(nums[n//2])
        # de = collections.deque(nums)
        # while (len(de)>1):
        #     x = de.pop()
        #     if x > root.val:
        #         root.right = self.insertt(root.right, x)
        #     else:
        #         root.left = self.insertt(root.left, x)
        # return root