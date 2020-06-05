# 107. Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

class Solution:
    # BFS
    def levelOrderBottom(self, root):

        q = []
        result = []
        if not root:
            return result

        q.append(root)

        while q:
            level_list = []
            level_size = len(q)
            # 不能直接用 range(len(q))，因为len(q)会变！
            for _ in range(level_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_list.append(node.val)
            result.insert(0, level_list)

        return result