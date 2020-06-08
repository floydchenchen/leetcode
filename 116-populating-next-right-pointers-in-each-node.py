# 116. Populating Next Right Pointers in Each Node

# Given a binary tree
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level,
# and every parent has two children).
# Example:
#
# Given the following perfect binary tree,
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # recursive solution
    def connect(self, root):
        if not root or not root.left:
            return
        root.left.next = root.right

        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    # iterative solution
    def connect1(self, root):
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next


    # universal iterative solution for 116 and 117
    def connect(self, root):
        cur = root
        # �����loop��cur node�����ƶ���ͨ��down_ptr������¼
        while cur:
            # create two dummy pointer nodes
            right_ptr, down_ptr = Node(-1), Node(-1)
            # ֻ��down_ptrָ����һ������ߵ�node�������ҵ��Ժ�Ͳ�����
            down_ptr_found = False
            # �����loop��cur node�����ƶ���ͨ��right_ptr������¼
            while cur:
                # ������Ϊdown_ptr��right_ptr�ʼ��һ��node������������down_ptrָ����parent����һ������ߵ�node
                if cur.left:
                    if not down_ptr_found:
                        down_ptr.next = cur.left
                        down_ptr_found = True
                    right_ptr.next = cur.left
                    right_ptr = right_ptr.next
                if cur.right:
                    if not down_ptr_found:
                        down_ptr.next = cur.right
                        down_ptr_found = True
                    right_ptr.next = cur.right
                    right_ptr = right_ptr.next
                cur = cur.next
            cur = down_ptr.next
        return root
