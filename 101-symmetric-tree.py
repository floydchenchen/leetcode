# 101. Symmetric Tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    # recursive preorder solution, with helper to check left and right
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            return p.val == q.val and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)

        if not root:
            return True
        return is_mirror(root.left, root.right)

    # iterative solution, deque
    def isSymmetric_BFS(self, root):
        if not root:
            return True

        dq = deque()
        dq.append((root.left, root.right))
        while dq:
            left, right = dq.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val == right.val:
                dq.appendleft((left.left, right.right))
                dq.appendleft((left.right, right.left))
            else:
                return False
        return True
