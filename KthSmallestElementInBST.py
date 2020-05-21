# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def kth_smallest(root, k):
#     def inorder(curr):
#         nonlocal inord, retval
#         if curr.left:
#             if inorder(curr.left):
#                 return True
#         if k == inord:
#             retval = curr.val
#             return True
#         inord += 1
#         if curr.right:
#             if inorder(curr.right):
#                 return True
#
#     inord = 1
#     retval = None
#     inorder(root)
#     return retval

def kth_smallest(curr, k):
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node2.left = node1

print(kth_smallest(node5, 3))
