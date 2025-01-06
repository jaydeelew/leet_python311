def kthFromTheEnd(head, k):
    slow = head
    fast = head

    for _ in range(k):
        if fast is None:
            return None  # return None if there are fewer than k nodes
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

result = kthFromTheEnd(one, 2)
if result is not None:
    print(result.val)  # safely access .val if result is not None
else:
    print("No such element")  # handle the case where result is None
