# 199. Binary Tree Right Side View

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive solution that combines left an right child
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        # combine root, right and extra left
        return [root.val] + right + left[len(right):]

    # recursive solution with dfs helper
    def rightSideView_v2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        self.dfs(root, 0, view)
        return view

    def dfs(self, root, depth, view):
        if root:
            if depth == len(view):
                view.append(root.val)
            self.dfs(root.right, depth + 1, view)
            self.dfs(root.left, depth + 1, view)



    # BFS, queue, level order traversal solution
    def rightSideView_BFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        q = []
        q.append(root)
        while q:
            level_length = len(q)
            result.append(q[-1].val)
            for _ in range(level_length):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result