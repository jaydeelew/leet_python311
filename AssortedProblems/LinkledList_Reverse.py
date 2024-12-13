# reverse a singly linked list and return the head of the reversed list

# POINTERS BEFORE WHILE LOOP
# 1 --> 2 --> 3 --> None, P=None
# C

# AFTER WHILE LOOP ITERATION
# None <-- 1     2 --> 3 --> None
#          P     N
#                C

# AFTER WHILE LOOP ITERATION
# None <-- 1 <-- 2     3 --> None
#                P     N
#                      C

# AFTER WHILE LOOP ITERATION
# None <-- 1 <-- 2 <-- 3, N=None, C=None
#                      P

# return P


def reverse_sll(head):
    curr = head
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def print_list(head):
    curr = head

    print(curr.val, end="")
    curr = curr.next

    while curr is not None:
        print(f" --> {curr.val}", end="")
        curr = curr.next

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

print_list(one)
new_head = reverse_sll(one)
print_list(new_head)
