# 257. Binary Tree Paths

# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive DFS solution
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path, result):
            if not root.left and not root.right:
                result.append(path + str(root.val))
            if root.left:
                dfs(root.left, path + str(root.val) + "->", result)
            if root.right:
                dfs(root.right, path + str(root.val) + "->", result)

        result = []
        if not root:
            return result
        dfs(root, "", result)
        return result

    # iterative queue BFS solution
    def binaryTreePaths1(self, root):
        result = []
        if not root:
            return result
        # 把当前到这个点的path都存在queue里面
        q = [root, ""]
        while q:
            node, path = q.pop(0)
            if not node.left and not node.right:
                result.append(path + str(node.val))
            if node.left:
                q.append((node.left, path + str(node.val) + "->"))
            if node.right:
                q.append((node.right, path + str(node.val) + "->"))


    # iterative stack DFS solution
    def binaryTreePaths2(self, root):
        result = []
        if not root:
            return result
        stack = [root, ""]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))