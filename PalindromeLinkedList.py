# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


def is_palindrome(head):
    nodes = []

    curr = head
    while curr:
        nodes.append(curr.val)
        curr = curr.next

    curr = head
    while curr:
        if curr.val != nodes.pop():
            return False
        curr = curr.next

    return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_list(node1)
print(is_palindrome(node1))
