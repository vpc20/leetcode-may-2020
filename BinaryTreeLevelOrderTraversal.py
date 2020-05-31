# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
from collections import deque
from math import log


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    def dfs(curr, lvl):
        if lvl == len(result):
            result.append([curr.val])
        else:
            result[lvl].append(curr.val)
        if curr.left:
            dfs(curr.left, lvl + 1)
        if curr.right:
            dfs(curr.right, lvl + 1)

    if root is None:
        return []
    result = []
    dfs(root, 0)
    return result


# def level_order(self, root: TreeNode) -> List[List[int]]:
#     if not root:
#         return []
#     queue = deque([root])
#     result = []
#
#     while queue:
#         result.append([])
#         count = len(queue)
#         for _ in range(count):
#             node = queue.popleft()
#             result[-1].append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return result


arr = [3, 9, 20, None, None, 15, 7]
# arr = [1, 2, None, 3, None, None, None, 4, None, None, None, None, None, None, None, 5]
nodes = [TreeNode(v) if v else None for v in arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i]:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i]:
        node.right = nodes[right_idx]

print(level_order(root))

# 0                                                        0
# 1 2                                                      1
# 3 4 5 6                                                  2
# 7 8 9 10 11 12 13 14                                     3
# 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30          4

# (i+1) / 2 ** x = 1
# 2 ** x = 1 - (i +1)
# 2 ** x = -i
# log i+1  = x
