def kthFromTheEnd(head, k):
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head

print(kthFromTheEnd(one, 2).val)  # 4
