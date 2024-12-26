# 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k places.


def rotateRight(head, k):
    if not head:
        return None

    iter = slow = fast = head
    length = 0

    while iter is not None:
        length += 1
        iter = iter.next

    # if k is greater than the length of the list, we only need to rotate k % length times
    if k > length:
        k = k % length

    for _ in range(k):
        fast = fast.next

    # if k % length is zero, fast is None because of the loop above
    if fast is None:
        return head

    while fast.next:
        slow = slow.next
        fast = fast.next

    # connect the end of the list to the beginning
    fast.next = head
    # set the new head to the next node after slow
    head = slow.next
    # set the next node after slow to None since it is now the end of the list
    slow.next = None

    return head


def print_nodes(head):
    current = head

    while current:
        print(current.val, end=" ")
        current = current.next

    print()


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head

print_nodes(rotateRight(one, 1))
