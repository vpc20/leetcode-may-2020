# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the
# position(0 - indexed) in the linked list where tail connects to.If pos is -1, then there is no cycle in the linked
# list.
#
# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


def has_cycle(curr):
    nset = set()
    while curr:
        if curr in nset:
            return True
        nset.add(curr)
        curr = curr.next
    return False


vals = [1, 2, 3, 4, 5, 6, 7]
head = prev = ListNode(vals[0])
for val in vals[1:]:
    prev.next = ListNode(val)
    prev = prev.next

print_list(head)
print(has_cycle(head))
