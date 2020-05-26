# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the
# nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


# def merge_two_lists(l1, l2):
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#
#     if l1.val <= l2.val:
#         l1.next = merge_two_lists(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge_two_lists(l1, l2.next)
#         return l2

# def merge_two_lists(l1, l2):
#     if l1 is None:
#         if l2 is None:
#             return None
#         else:
#             return l2
#     else:
#         if l2 is None:
#             return l1
#
#     curr1 = l1
#     curr2 = l2
#     if curr1.val < curr2.val:
#         head = curr3 = curr1
#         curr1 = curr1.next
#     else:
#         head = curr3 = curr2
#         curr2 = curr2.next
#
#     while curr1 and curr2:
#         if curr1.val < curr2.val:
#             curr3.next = curr1
#             curr1 = curr1.next
#         else:
#             curr3.next = curr2
#             curr2 = curr2.next
#         curr3 = curr3.next
#
#     if curr1:
#         curr3.next = curr1
#
#     if curr2:
#         curr3.next = curr2
#
#     return head


def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    curr1 = l1
    curr2 = l2

    if curr1.val < curr2.val:
        head = curr3 = curr1
        curr1 = curr1.next
    else:
        head = curr3 = curr2
        curr2 = curr2.next

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr3.next = curr1
            curr1 = curr1.next
        else:
            curr3.next = curr2
            curr2 = curr2.next
        curr3 = curr3.next

    if curr1:
        curr3.next = curr1

    if curr2:
        curr3.next = curr2

    return head


# def merge_two_lists(l1, l2):
#     if l1 is None:
#         if l2 is None:
#             return None
#         else:
#             return l2
#     else:
#         if l2 is None:
#             return l1
#
#     curr1 = l1
#     curr2 = l2
#     if curr1.val < curr2.val:
#         head = curr1
#     else:
#         head = curr2
#
#     while curr1 and curr2:
#         next1 = curr1.next
#         next2 = curr2.next
#         if curr1.val < curr2.val:
#             curr1.next = curr2
#         else:
#             curr2.next = curr1
#
#         if next1 is None:
#             tail1 = curr1
#         if next2 is None:
#             tail2 = curr2
#
#         curr1 = next1
#         curr2 = next2
#
#     if curr1:
#         tail2.next = curr1
#
#     if curr2:
#         tail1.next = curr2
#
#     return head


# node1 = ListNode(1)
# node2 = ListNode(2)
# node4 = ListNode(4)
#
# nodea1 = ListNode(1)
# nodea3 = ListNode(3)
# nodea4 = ListNode(4)
#
# node1.next = node2
# node2.next = node4
#
# nodea1.next = nodea3
# nodea3.next = nodea4
#
# print_list(node1)
# print_list(nodea1)


node5 = ListNode(5)

nodea1 = ListNode(1)
nodea2 = ListNode(2)
nodea4 = ListNode(4)

nodea1.next = nodea2
nodea2.next = nodea4

print_list(node5)
print_list(nodea1)

print_list(merge_two_lists(node5, nodea1))
