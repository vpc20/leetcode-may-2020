# Write a program to find the node at which the intersection of two singly linked lists begins.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


def get_intersection_node(heada, headb):
    seta = set()
    curr = heada
    while curr:
        seta.add(curr)
        curr = curr.next

    curr = headb
    while curr:
        if curr in seta:
            return curr
        curr = curr.next

    return None
