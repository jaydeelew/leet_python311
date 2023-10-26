class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return head

        d = Node(-1)
        d1 = None
        h = head

        while h:
            t = Node(h.val)
            t.next = h.next
            t.random = h.random
            h.next = t
            h = t.next

        h = head.next

        while h:
            t = h
            if t.random:
                t.random = t.random.next
            if h.next:
                h = h.next.next
            else:
                break

        h = head
        d = head.next
        d1 = d

        while h:
            if not d.next:
                h.next = None
                break
            h.next = d.next
            d.next = h.next.next
            h = h.next
            d = d.next

        return d1

    def printLinkedList(self, head: "Node"):
        curr_node = head
        while curr_node:
            randomPtr = None
            if curr_node.random:
                randomPtr = curr_node.random.val
            print(str(curr_node.val) + " " + str(randomPtr))
            curr_node = curr_node.next


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

# head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
sol = Solution()
sol.printLinkedList(seven)
sol.printLinkedList(sol.copyRandomList(seven))
