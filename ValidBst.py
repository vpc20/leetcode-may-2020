import sys
from collections import deque


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


def print_inorder(curr):
    if curr.left is not None:
        print_preorder(curr.left)
    print(curr.val, end=' ')
    if curr.right is not None:
        print_preorder(curr.right)


def is_valid_bst(root):
    def inorder(curr):
        nonlocal prevval
        if curr.left:
            if inorder(curr.left) is False:
                return False

        if prevval is not None and curr.val <= prevval:
            return False
        else:
            prevval = curr.val

        if curr.right:
            if inorder(curr.right) is False:
                return False
        return True

    if root is None:
        return True
    prevval = None
    return inorder(root)


def is_valid_bst_iter(root):
    if root is None:
        return True
    q = deque([(root, -sys.maxsize, sys.maxsize)])
    while q:
        curr, lo, hi = q.popleft()
        val = curr.val
        if lo >= val or hi <= val:
            return False
        if curr.left:
            q.append((curr.left, lo, val))
        if curr.right:
            q.append((curr.right, val, hi))
    return True


def is_valid_bstx(curr):
    prevval = -sys.maxsize
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if prevval >= curr.val:
                return False
            else:
                prevval = curr.val
            curr = curr.right
    return True


#              10
#       5              15
#                  6        20

# arr = [1, 2, 3, None, 4, None, 5]
arr = [10, 5, 15, None, None, 6, 20]

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
print_inorder(root)
print('')

print(is_valid_bst(root))
print(is_valid_bst_iter(root))
