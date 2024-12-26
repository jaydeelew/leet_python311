# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


def removeNthFromEnd(head, n):
    prev = slow = fast = head

    for _ in range(n - 1):
        fast = fast.next
        if not fast:
            return None

    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next

    if slow == head:
        head = head.next

    prev.next = slow.next

    return head


def printNodes(head):
    if not head:
        print(None, end="")

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

k = 2
# Output: 1 2 3 5

printNodes(removeNthFromEnd(one, k))
