# 141. Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer.
# Return true if there is a cycle in the linked list. Otherwise, return false.


def hasCycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head
five.next = one  # create cycle

print(hasCycle(one))
