# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursive divide and conquer
    def minDepth(self, root):
        if not root:
            return 0
        left, right = self.minDepth(root.left), self.minDepth(root.right)
        # note that one of left and right child could be null, we need to count the non-null child in this case.
        return 1 + min(left, right) if left and right else 1 + left + right

    # BFS
    def minDepth(self, root):
        if not root:
            return 0
        q = [root]
        depth = 1

        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

