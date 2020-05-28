# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Follow up: Solve it both recursively and iteratively.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def is_sym(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and is_sym(root1.left, root2.right) and is_sym(root1.right, root2.left)

    return is_sym(root, root)


# def is_symmetric(root):
#     def is_sym(root1, root2):
#         if root1 is None and root2 is None:
#             return True
#         if root1 is None or root2 is None:
#             return False
#         if root1.val != root2.val:
#             return False
#         if not is_sym(root1.left, root2.right):
#             return False
#         if not is_sym(root1.right, root2.left):
#             return False
#         return True
#
#     return is_sym(root, root)


def is_symmetric_iter(root):
    q = deque([root, root])

    while q:
        t1 = q.popleft()
        t2 = q.popleft()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        q.append(t1.left)
        q.append(t2.right)
        q.append(t1.right)
        q.append(t2.left)

    return True


# arr = [1]
# arr = [1, 2]
# arr = [1, 2, 3]
# arr = [1, 2, 2]
# arr = [1, 2, 2, 3, 4, 4, 3]
arr = [1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5]
nodes = [TreeNode(v) if v else None for v in arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

# print(is_symmetric(None))
print(is_symmetric(root))
print(is_symmetric_iter(root))
