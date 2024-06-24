# def fn(head):
#     curr = head
#     prev = None
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node

#     return prev


# reverse a singly linked list and return the head of the reversed list
def reverse_sll(head):
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)  # head

new_head = reverse_sll(one)
print("breakpoint this line to explore new_head")
