# 109. Convert Sorted List to Binary Search Tree

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # we need to get the median in the sorted list, so we need fast and slow runners
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def dfs(start, end):
            fast = slow = start

            # exit case
            if start == end:
                return None

            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next

            # median / root node
            node = TreeNode(slow.val)
            node.left = dfs(start, slow)
            node.right = dfs(slow.next, end)
            return node

        if not head:
            return None
        # the ending ListNode is None in the list
        return dfs(head, None)


    # recursive divide and conquer solution
    def sortedListToBST1(self, head):
        # convert linked list to an array and build the BST
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def sortedArrayToBST(nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid + 1:])
            return root

        return sortedArrayToBST(nums)