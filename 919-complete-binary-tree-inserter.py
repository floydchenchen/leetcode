# 919. Complete Binary Tree Inserter

# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
# and all nodes are as far left as possible.
#
# Write a data structure CBTInserter that is initialized with a complete binary tree
# and supports the following operations:
#
# CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v
# so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
#
#
# Example 1:
#
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
#
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = [root]
        # inorder traversal
        for node in self.tree:
            if node.left:
                self.tree.append(node.left)
            if node.right:
                self.tree.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        n = len(self.tree)
        self.tree.append(TreeNode(v))
        if n % 2 == 0:
            self.tree[(n-1)//2].right = self.tree[-1]
        else:
            self.tree[(n-1)//2].left = self.tree[-1]
        return self.tree[(n-1)//2].val



    # def insert_helper(self, node, v):
    #     if not node.left:
    #         node.left = TreeNode(v)
    #         return node.val
    #     elif not node.right:
    #         node.right = TreeNode(v)
    #         return node.val
    #     elif not self.isFull(node.left):
    #         return self.insert_helper(node.left, v)
    #     elif not self.isFull(node.right) or self.getLevel(node.right) < self.getLevel(node.left):
    #         return self.insert_helper(node.right, v)
    #     else:
    #         return self.insert_helper(node.left, v)


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.tree[0]

    # def isFull(self, node):
    #     if not node:
    #         return True
    #
    #     if not node.left and not node.right:
    #         return True
    #
    #     if node.left and node.right:
    #         return self.isFull(node.left) and self.isFull(node.right) and self.getLevel(node.left) == self.getLevel(node.right)
    #
    #     return False
    #
    # def getLevel(self, node):
    #     if not node:
    #         return 0
    #     return 1 + max(self.getLevel(node.left), self.getLevel(node.right))

root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

t = CBTInserter(root)
print(t.insert(2))
print(t.insert(3))
print(t.insert(4))
print(t.insert(5))
print(t.insert(6))
print(t.insert(7))
print(t.insert(8))
print(t.insert(9))
print("left full", t.isFull(t.root))