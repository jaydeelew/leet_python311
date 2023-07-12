import copy


# this implementation of a DLL uses sentinels
class DLL:
    class ListNode:
        def __init__(self, val, prev, next):
            self.value = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.ListNode(None, None, None)
        self.tail = self.ListNode(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, val):
        new_node = self.ListNode(val, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def add_rear(self, val):
        new_node = self.ListNode(val, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def rem_front(self):
        self.head.next.next.prev = self.head  # assign head to prev pointer of the node after next
        self.head.next = self.head.next.next  # assign node after next to be next node

    def rem_rear(self):
        self.tail.prev.prev.next = self.tail  # asssign tail to the next pointer of the node before previous
        self.tail.prev = self.tail.prev.prev  # assign node before previous to be the previous node

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def del_node(self, val):
        node_ptr = self.head
        while node_ptr.next.value:
            if node_ptr.next.value == val:
                node_ptr.next.next.prev = node_ptr
                node_ptr.next = node_ptr.next.next
                return
            node_ptr = node_ptr.next

    def get_sum(self):
        ans = 0
        node_ptr = self.head.next
        while node_ptr.value:
            ans += node_ptr.value
            node_ptr = node_ptr.next
        print(ans)

    def print_middle(self):
        if self.head.next is not None:
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.value)

    def hasCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        print(False)

    def find_k_node(self, k):  # find kth node from end
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        print(slow.prev.value)

    def del_duplicates(self):  # using two pointers
        current = self.head
        following = self.head.next
        while following != self.tail:
            if current.value == following.value:
                current.next = following.next  # skip next node by assigning following node's next to current node's next
                following.next.prev = current  # skip next node also by assignning following node's next's prev to current node
                following = following.next  # the node after following becomes the new following node
            else:
                current = current.next
                following = following.next

    def reverse_list(self):
        current = self.head.next
        reversed = DLL()
        while current != self.tail:
            reversed.add_front(current.value)
            current = current.next
        reversed.print_nodes()

    def copy_list(self):
        return copy.deepcopy(dll)

    def reverse_sll(self):
        copied_list = self.copy_list()  # using as a SLL
        curr_node = copied_list.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next  # must save next node since pointer to it is changed on line below
            curr_node.next = prev_node  # have current node now point to previous node
            prev_node = curr_node  # set previous node to current node
            curr_node = next_node  # make next node the current node
        return prev_node  # this last node of original list becomes the first in reversed list

    def reverse_dll(self):
        copied_list = self.copy_list()
        curr_node = copied_list.head
        while curr_node:
            next_node = curr_node.next  # must save next node since it is changed on line below
            curr_node.next = curr_node.prev  # the current node's next becomes the current node's previous
            curr_node.prev = next_node  # the current node's previous becomes the current node's next
            curr_node = next_node  # the current node is assigned next node
        return copied_list.tail

    def reverse_sll_between(self, left, right):
        copied_list = self.copy_list()
        prev_node = copied_list.head
        curr_node = until_node = copied_list.head.next
        for _ in range(left - 1):
            prev_node = curr_node
            curr_node = curr_node.next
        for _ in range(right - 1):
            until_node = until_node.next

        terminate_loop = until_node.next  # save until.node.next since it will change
        resume_node = curr_node
        prev_node.next = until_node
        prev_node = curr_node
        curr_node = curr_node.next

        while curr_node != terminate_loop and curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        resume_node.next = curr_node
        return copied_list.head

    def print_nodes(self, outside_head=None):
        if outside_head is None:
            node_ptr = self.head.next
        else:
            node_ptr = outside_head.next
        while node_ptr and node_ptr.value:  # if node_ptr is None, end loop before accessing node_ptr.value
            print(node_ptr.value, end=" ")
            node_ptr = node_ptr.next
        print("")


dll = DLL()
dll.add_rear("1")
# dll.add_rear("2")
# dll.add_rear("3")
# dll.add_rear("4")
# dll.add_rear("5")
