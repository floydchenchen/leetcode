# 889. Construct Binary Tree from Preorder and Postorder Traversal
# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
# # preorder = [1,2,4,5,3,6,7]
# # postorder = [4,5,2,6,7,3,1]
# # Return the following binary tree:
# #
# #     1
# #    / \
# #   2   3
# #  / \  /\
# # 4  5 6  7

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：preorder的第一个和postorder的最后一个是root，分别将它们pop出来
# 接下来preorder第一个是left child，postorder最后一个是right child
# 利用left child在postorder中，或者利用right child在preorder中做分割
# recursive divide and conquer
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder.pop(0))
        # 注意edge case
        if len(postorder) == 1:
            return root
        postorder.pop()
        right_child = postorder[-1]
        right_child_index = preorder.index(right_child)
        root.left = self.constructFromPrePost(preorder[:right_child_index], postorder[:right_child_index])
        root.right = self.constructFromPrePost(preorder[right_child_index:], postorder[right_child_index:])
        return root
