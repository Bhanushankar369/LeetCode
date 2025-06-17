# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        level = []

        while q:
            node = q.popleft()
            if node:
                level.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                level.append("#")

        while level and level[-1] == "#":
            level.pop()
        
        return ",".join(level)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data[0] == "#":
            return None
        lst = data.split(",")
        root = TreeNode(int(lst[0]))
        q = deque([root])

        i=1
        while q and i<len(lst):
            node = q.popleft()

            if lst[i] == "#":
                node.left = None
            else:
                node.left = TreeNode(int(lst[i]))
                q.append(node.left)
            i+=1

            if i<len(lst) and lst[i] == "#":
                    node.right = None
            else:
                if i<len(lst):
                    node.right = TreeNode(int(lst[i]))
                    q.append(node.right)
            i+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))