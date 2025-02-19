# 0. Implement a doubly linked list class using sentinels.
# [Head Sentinel] <-> [Data Node 1] <-> [Data Node 2] <-> [Tail Sentinel]
import copy


class DLL:
    class ListNode:
        def __init__(self, val, prev=None, next=None):
            self.value = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.ListNode(None, None, None)
        self.tail = self.ListNode(None, None, None)
        self.tail.prev = self.head
        self.head.next = self.tail

    def add_front(self, val):
        new_node = self.ListNode(val, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node

    def add_rear(self, val):
        new_node = self.ListNode(val, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def array_to_ll(self, arr):
        for val in arr:
            self.add_rear(val)

    def rem_front(self):
        # assign head to prev pointer of the node after next
        self.head.next.next.prev = self.head
        # assign node after next to be next node
        self.head.next = self.head.next.next

    def rem_rear(self):
        # asssign tail to the next pointer of the node before previous
        self.tail.prev.prev.next = self.tail
        # assign node before previous to be the previous node
        self.tail.prev = self.tail.prev.prev

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
        return ans

    def return_middle(self):
        if self.head.next is not None:
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

    def hasCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # find kth node from end
    def find_kth_node(self, k):
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow

    # using two pointers
    def del_duplicates(self):
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

    def copy_list(self):
        return copy.deepcopy(dll)

    def reverse_list(self):
        current = self.head.next
        reversed = DLL()
        while current != self.tail:
            reversed.add_front(current.value)
            current = current.next
        reversed.print_nodes()

    def reverse_dll(self):
        copied_list = self.copy_list()
        curr_node = copied_list.head
        while curr_node:
            # must save next node since it is changed on line below
            next_node = curr_node.next
            # the current node's next becomes the current node's previous
            curr_node.next = curr_node.prev
            # the current node's previous becomes the current node's next
            curr_node.prev = next_node
            # the current node is assigned next node
            curr_node = next_node
        return copied_list.tail

    def print_nodes(self, outside_head=None):
        if outside_head is None:
            node_ptr = self.head.next
        else:
            node_ptr = outside_head.next
        # if node_ptr is None, end loop before accessing node_ptr.value
        while node_ptr and node_ptr.value:
            print(node_ptr.value, end=" ")
            node_ptr = node_ptr.next
        print("")


dll = DLL()
arr = [1, 2, 3, 4, 5]
dll.array_to_ll(arr)
dll.print_nodes()
