# 117. Populating Next Right Pointers in Each Node II

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
# Example:
#
# Given the following binary tree,
#
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # interative solution
    def connect(self, root: 'Node') -> 'Node':
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
                    right_ptr.next = cur.left
                    if not down_ptr_found:
                        down_ptr.next = cur.left
                        down_ptr_found = True
                    right_ptr = cur.left
                if cur.right:
                    right_ptr.next = cur.right
                    if not down_ptr_found:
                        down_ptr.next = cur.right
                        down_ptr_found = True
                    right_ptr = cur.right
                cur = cur.next
            cur = down_ptr.next
        return root