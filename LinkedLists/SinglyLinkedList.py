import copy


class SLL:
    class ListNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def add_array(self, arr):
        for element in arr:
            self.add_rear(element)

    def add_front(self, val):
        new_node = self.ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def add_rear(self, val):
        new_node = self.ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            node_ptr = self.head
            while node_ptr.next is not None:
                node_ptr = node_ptr.next
            node_ptr.next = new_node

    def rem_front(self):
        if self.head is not None:
            self.head = self.head.next

    def rem_rear(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                return
            curr_node = self.head
            while curr_node.next.next is not None:
                curr_node = curr_node.next
            curr_node.next = None

    def del_node(self, val):
        if self.head is not None:
            if self.head.val == val:
                self.head = self.head.next
                return
            curr_node = self.head
            while curr_node.next is not None:
                if curr_node.next.val == val:
                    curr_node.next = curr_node.next.next
                    return
                curr_node = curr_node.next

    def print_sum(self):
        sum = 0
        curr_node = self.head
        while curr_node is not None:
            sum += curr_node.val
            curr_node = curr_node.next
        print(sum)

    def copy_list(self):
        return copy.deepcopy(sll)

    # recursive
    def get_sum(self, head):
        curr_node = head
        # if there is no node beside head node
        if curr_node is None:
            return 0
        # when curr_node.next becomes None, we are on the last node - base case
        if curr_node.next is None:
            # return val from last node
            return curr_node.val
        # return curr_node head val + retrn value of this function
        return curr_node.val + self.get_sum(curr_node.next)

    def print_middle(self):
        if self.head is not None:
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.val)

    def reverse_sll(self):
        if self.head is not None:
            if self.head.next is None:
                return self.head
            else:
                prev_node = None
            curr_node = self.head
            while curr_node is not None:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            return prev_node

    def swap_node_pairs(self):
        if self.head is not None:
            if self.head.next is None:
                return self.head
            prev_node = curr_node = self.head
            # second node will be first node in swapped list
            new_head_node = curr_node.next
            # curr_node becomes None odd sz list. curr_node.next becomes None even sz list
            while curr_node and curr_node.next:
                # next two lines are redundant on the first iteration
                # after curr_node points to recover_node at end of previous loop,
                prev_node.next = curr_node.next
                # prev_node.next now points to second node on previously-detached part of list
                prev_node = curr_node

                # save ptr to node after next. list will be detached at this point on ln below
                recover_node = curr_node.next.next
                # node after curr_node now points back to curr_node
                curr_node.next.next = curr_node
                # this is where swapped part of list reattaches with rest of list
                curr_node.next = recover_node
                # curr_node now set to work on unswapped part of list
                curr_node = recover_node
            return new_head_node

    def reverse_sll_between(self, left, right):
        if self.head is not None:
            if self.head.next is None:
                return self.head
            if left == 1 and right == 1:
                return self.head

            prev_node = curr_node = until_node = self.head

            for _ in range(left - 1):
                prev_node = curr_node
                curr_node = curr_node.next
            for _ in range(right - 1):
                until_node = until_node.next
            if curr_node == self.head:
                curr_node = curr_node.next

            prev_node.next = until_node
            term_node = until_node.next
            resu_node = curr_node

            while curr_node != term_node:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

            if left == 1:
                self.head.next = term_node
                self.head = until_node
            else:
                resu_node.next = term_node

            return self.head

    def delete_middle(self):
        if self.head is not None:
            if self.head.next is None:
                return None
            prev_node = None
            fast = slow = self.head
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                prev_node = slow
                slow = slow.next
            prev_node.next = slow.next
            return self.head

    def rem_Nth_from_end(self, n):
        if self.head is not None and n != 0:
            if self.head.next is None and n == 1:
                return None
            if n == 1:
                return None
            prev_node = None
            slow = fast = self.head
            for _ in range(n):
                fast = fast.next
            while fast is not None:
                prev_node = slow
                slow = slow.next
                fast = fast.next
            if prev_node is None:
                self.head = self.head.next
            else:
                prev_node.next = slow.next
            return self.head

    def is_palindrome(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev_node = slow
        curr_node = slow.next
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        slow.next = None
        head_one = self.head
        head_two = prev_node

        while head_two:
            if head_one.val != head_two.val:
                return False
            head_one = head_one.next
            head_two = head_two.next
            return True

    def remove_same_element(self, val):
        while self.head and self.head.val == val:
            self.head = self.head.next
        if self.head:
            curr_node = self.head
            while curr_node.next:
                while curr_node.next and curr_node.next.val == val:
                    curr_node.next = curr_node.next.next
                if curr_node.next is not None:
                    curr_node = curr_node.next
                else:
                    break
            return self.head

    def odd_even_list(self):
        if self.head:
            odd_node = self.head
            even_head = even_node = self.head.next
            while odd_node.next and even_node.next:
                odd_node.next = odd_node.next.next
                even_node.next = even_node.next.next
                odd_node = odd_node.next
                even_node = even_node.next
            odd_node.next = even_head
            return self.head

    def print_nodes(self, outside_head=None):
        if outside_head is None:
            node_ptr = self.head
        else:
            node_ptr = outside_head
        while node_ptr:
            print(node_ptr.val, end=" ")
            node_ptr = node_ptr.next
        print("")


sll = SLL()
sll.add_rear(1)
sll.add_rear(2)
sll.add_rear(3)
sll.add_rear(4)
sll.add_rear(5)
sll.print_nodes()
sll.print_nodes(sll.delete_middle())
