# 297. Serialize and Deserialize Binary Tree
# Serialization is the process of converting a data structure or object into a sequence of bits so that
# it can be stored in a file or memory buffer, or transmitted across a network connection link to be
# reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # preorder traversal
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root:
            return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)
        else:
            return "#"


    # DFS解法, 相当于construct binary tree from preorder traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        q = data.split()
        def dfs(q):
            if not q:
                return None
            val = q.pop(0)
            if val == "#":
                return None
            else:
                node = TreeNode(val)
                node.left = dfs(q)
                node.right = dfs(q)
            return node
        return dfs(q)







# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(codec.serialize(root))