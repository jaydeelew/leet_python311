# 138. Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer,
# which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
# where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in
# the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
# then for the corresponding two nodes x and y in the copied list, x.random --> y.
# Return the head of the copied linked list.
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
# - val: an integer representing Node.val
# - random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
# or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    oldToCopy = {None: None}

    curr = head

    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy[curr.next]
        copy.random = oldToCopy[curr.random]
        curr = curr.next

    return oldToCopy[head]


def printLinkedList(head):
    ans = []
    curr_node = head
    while curr_node:
        randomPtr = None
        if curr_node.random:
            randomPtr = curr_node.random.val
        ans.append([curr_node.val, randomPtr])
        curr_node = curr_node.next
    print(ans)


# Test case setup
# Creating a linked list: 7 -> 13 -> 11 -> 10 -> 1
# with random pointers: [7,null] -> [13,7] -> [11,1] -> [10,11] -> [1,7]
one = Node(1)
ten = Node(10)
eleven = Node(11)
thirteen = Node(13)
seven = Node(7)  # head

one.next = None
one.random = seven
ten.next = one
ten.random = eleven
eleven.next = ten
eleven.random = one
thirteen.next = eleven
thirteen.random = seven
seven.next = thirteen
seven.random = None

# Print original and copied list to verify the copy
print("Original list:")
printLinkedList(seven)
print("Copied list:")
printLinkedList(copyRandomList(seven))
