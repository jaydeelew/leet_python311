# def fn(head):
#     slow = head
#     fast = head
#     ans = 0

#     while fast and fast.next:
#         # do logic
#         slow = slow.next
#         fast = fast.next.next

#     return ans


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head
# five.next = one

# only run if list does not have a cycle
print(get_middle(one))
# print(hasCycle(one))
