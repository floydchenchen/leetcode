# 426. Convert Binary Search Tree to Sorted Doubly Linked List

# Convert a BST to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
#
# Let's take the following BST as an example, it may help you understand the problem better:
#
#
#
#
#
# We want to transform this BST into a circular doubly linked list.
# Each node in a doubly linked list has a predecessor and successor.
# For a circular doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
#
# The figure below shows the circular doubly linked list for the BST above.
# The "head" symbol means the node it points to is the smallest element of the linked list.
#
#
#
#
#
# Specifically, we want to do the transformation in place.
# After the transformation, the left pointer of the tree node should point to its predecessor,
# and the right pointer should point to its successor.
# We should return the pointer to the first element of the linked list.
#
# The figure below shows the transformed BST.
# The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def inorder_traversal(node):
            # exit
            if not node.left and not node.right:
                # if no children, left and right should point to the node itself
                return node, node
            if node.left:
                left_start, left_end = inorder_traversal(node.left)
                # connecting left_end with node
                left_end.right = node
                node.left = left_end
            else:
                left_start, left_end = node, node

            if node.right:
                right_start, right_end = inorder_traversal(node.right)
                # connecting node with right_start
                node.right = right_start
                right_start.left = node
            else:
                right_start, right_end = node, node
            return left_start, right_end

        if not root:
            return None
        left_start, right_end = inorder_traversal(root)
        right_end.right = left_start
        left_start.left = right_end
        return left_start

root = Node(4, None, None)
root.left = Node(2, None, None)
root.right = Node(5, None, None)
root.left.left = Node(1, None, None)
root.left.right = Node(3, None, None)

sol = Solution()
print(sol.treeToDoublyList(root))