class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_preorder(curr):
    print(curr.val, end=' ')
    if curr.left is not None:
        print_preorder(curr.left)
    if curr.right is not None:
        print_preorder(curr.right)


def max_depth(root):
    if root is None:
        return 0
    left = right = 1
    if root and root.left:
        left = 1 + max_depth(root.left)
    if root and root.right:
        right = 1 + max_depth(root.right)
    return max(left, right)


# arr = [3, 9, 20, None, None, 15, 7]
arr = [3, 9, 20, None, None, 15, 7]
nodes = [TreeNode(v) if v else None for v in arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

print_preorder(root)
print('')

print(max_depth(root))
