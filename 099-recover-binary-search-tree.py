# 99. Recover Binary Search Tree

# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
# Input: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# Output: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# Example 2:
#
# Input: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# Output: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3
# Follow up:
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import math


# 这道题目还是利用二叉查找树的主要性质，就是中序遍历是有序。那么如果其中有元素被调换了，意味着中序遍历中必然出现违背有序的情况。
class Solution:
    def __init__(self):
        self.first = self.second = TreeNode(None)
        self.prev = TreeNode(-math.inf)

    # recursive in-order traversal for BST
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder_traversal(root)
        # swap
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        # left ->
        self.inorder_traversal(root.left)
        # -> current, prevNode should always be less than current node
        if self.first.val is None and self.prev.val >= root.val:
            self.first = self.prev
        if self.first.val is not None and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        # -> right
        self.inorder_traversal(root.right)

    
    # iterative solution
    def recoverTree1(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = prev = None
        
        while stack or root:
            # left 
            while root:
                stack.append(root)
                root = root.left
            # root
            root = stack.pop()
            if prev and root.val < prev.val:
                y = root
                if x is None:
                    x = prev 
                else:
                    break
            prev = root
            # right
            root = root.right

        x.val, y.val = y.val, x.val