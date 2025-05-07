# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummyNode = ListNode(-1)
    temp = dummyNode

    curr1, curr2 = list1, list2

    while curr1 and curr2:
        if curr1.val < curr2.val:
            temp.next = curr1
            curr1 = curr1.next
        else:
            temp.next = curr2
            curr2 = curr2.next
        temp = temp.next

    temp.next = curr1 if curr1 else curr2

    return dummyNode.next


def print_list(head):
    node = head
    ll = []
    while node is not None:
        ll.append(node.val)
        node = node.next

    print(ll)


# four_1 = ListNode(4)
# two_1 = ListNode(2, four_1)
# one_1 = ListNode(1, two_1)

# four_2 = ListNode(4)
# three_2 = ListNode(3, four_2)
# one_2 = ListNode(1, three_2)

# Output: [1,1,2,3,4,4]

# one = ListNode(1)
# two = ListNode(2)
# Output: [2, 1]

five = ListNode(5)

four = ListNode(4)
two = ListNode(2, four)
one = ListNode(1, two)

print_list(mergeTwoLists(five, one))
