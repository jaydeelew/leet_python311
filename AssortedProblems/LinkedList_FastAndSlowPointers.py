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
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def kth_from_end(head, k):
    slow = fast = head

    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow.val


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def rotate_right_k_times(head, k):
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


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head
# five.next = one  # create cycle
no_node = None

# only run if list does not have a cycle
print(get_middle(one))
print(kth_from_end(one, 1))
print(has_cycle(one))
print_nodes(rotate_right_k_times(one, 1))
print()
