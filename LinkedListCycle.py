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


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print_list(node1)
print(has_cycle(node1))
