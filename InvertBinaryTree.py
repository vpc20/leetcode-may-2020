# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


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


def print_preorder_inverted(curr):
    print(curr.val, end=' ')
    if curr.right:
        print_preorder_inverted(curr.right)
    if curr.left:
        print_preorder_inverted(curr.left)


def invert_tree(root):
    if root is None:
        return root
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


node4 = TreeNode(4)
node2 = TreeNode(2)
node7 = TreeNode(7)
node1 = TreeNode(1)
node3 = TreeNode(3)
node6 = TreeNode(6)
node9 = TreeNode(9)

node4.left = node2
node4.right = node7
node2.left = node1
node2.right = node3
node7.left = node6
node7.right = node9

print_preorder(node4)
print('')
print_preorder_inverted(node4)
print('')

print_preorder(invert_tree(node4))
