# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
# are overlapped while the others are not.
#
# You need to merge them into a new binary tree.The merge rule is that if two nodes overlap, then sum node values
# up as the new value of the merged node.Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
#
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
# Note: The merging process must start from the root nodes of both trees.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_preorder(curr):
    print(curr.val, end=' ')
    if curr.left:
        print_preorder(curr.left)
    if curr.right:
        print_preorder(curr.right)


def merge_trees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)
    return t1


# treea1 = TreeNode(1)
# treea3 = TreeNode(3)
# treea2 = TreeNode(2)
# treea5 = TreeNode(5)
#
# treea1.left = treea3
# treea1.right = treea2
# treea3.left = treea5
#
# print_preorder(treea1)
# print('')
#
# treeb2 = TreeNode(2)
# treeb1 = TreeNode(1)
# treeb3 = TreeNode(3)
# treeb4 = TreeNode(4)
# treeb7 = TreeNode(7)
#
# treeb2.left = treeb1
# treeb2.right = treeb3
# treeb1.right = treeb4
# treeb3.right = treeb7
#
# print_preorder(treeb2)
# print('')

arr = [1, 3, 2, 5]
nodes = [TreeNode(v) if v else None for v in arr]
root1 = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

print_preorder(root1)
print('')

arr = [2, 1, 3, None, 4, None, 7]
nodes = [TreeNode(v) if v else None for v in arr]
root2 = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

print_preorder(root2)
print('')

print_preorder(merge_trees(root1, root2))
