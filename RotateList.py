class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(curr):
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print('')


def rotate_list(head, k):
    curr = head
    i = 1
    while curr.next:
        if i == k:
            new_tail = curr
            new_head = curr.next
        i += 1
        curr = curr.next
    tail = curr
    tail.next = head
    new_tail.next = None
    return new_head


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
print_list(rotate_list(node1, 2))
