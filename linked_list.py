class Node:
    def __init__(self, data):
        # Pg 92
        self.data = data
        self.next = None

    def __str__(self):
        result = str(self.data)
        node = self
        while node.next != None:
            node = node.next
            result += ", " + str(node.data)
        return result

    def kth_to_last_recursive(self, k, i):
        print(self, k, i)
        if self == None or self.next == None:
            return 0
        i += 1
        node = self.next.kth_to_last_recursive(k, i)
        print(k, i)
        if i == k:
            print("  ", i, k)
            return self.data
        return node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append_to_tail(self, data):
        # Pg 92
        end = Node(data)
        node = self.head

        while node.next != None:
            node = node.next
        node.next = Node(data)

    def append_to_head(self, data):
        head = Node(data)
        head.next = self.head
        self.head = head
        
    def delete_node(self, data):
        # Pg 93
        # If the list has no nodes
        if self.head == None:
            return None

        # If the node to delete is first
        if self.head.data == data:
            return self.head.next

        node = self.head
        while node.next != None:
            if node.next.data == data:
                node.next = node.next.next
                return self.head
            node = node.next
        return self.head

    def __str__(self):
        return str(self.head)

    def remove_dups(self):
        # Pg 94, Q2.1
        used = []

        # If the list is empty or only 1 element, there is nothing to remove
        if self.head == None or self.head.next == None:
            return self

        previous = None
        node = self.head

        while node != None:            
            if node.data in used:
                previous.next = node.next
            else:
                used.append(node.data)
                previous = node

            node = node.next

    def remove_dups_no_buffer(self):
        # Pg 94, Q2.1
        slow = self.head
        while slow != None:
            fast = slow
            while fast.next != None:
                if fast.next.data == slow.data:
                    fast.next = fast.next.next
                else:
                    fast = fast.next
            slow = slow.next

    def kth_to_last_given_size(self, k, size):
        # Pg 94, Q2.2
        node = self.head

        index = size - k - 1
        for i in range(index):
            node = node.next
        
        return node.data

    def kth_to_last_recursive(self, k):
        # Pg 94, Q2.2
        return self.head.kth_to_last_recursive(k, 0)

    def kth_to_last_pointers(self, k):
        slow = self.head
        fast = self.head

        # Move fast node ahead by k
        for i in range(k):
            if fast == None:
                return None
            fast = fast.next

        # Iterate until fast is at the end and slow is at kth from last
        while fast.next != None:
            fast = fast.next
            slow = slow.next 
        return slow.data

    def delete_middle_node(self, c):
        # Pg 94, Q2.3

        # If the node is at the end or empty, return false - failure
        if c == None or c.next == None:
            return False

        # Otherwise, copy the contents of the next node
        # then delete the next node
        c.data = c.next.data
        c.next = c.next.next
        return True

    def partition(self, val):
        # Pg 94, Q2.4
        # FIX MEEEEEEEE
        slow = self.head

        while slow != None:
            print(self)
            if slow.data < val:
                print("  ", slow.data)
                slow = slow.next
            # If slow is bigger than or equal to val, bubble it up
            else:
                fast = slow
                temp = fast.data
                while fast.next != None:
                    print(self, "\n", slow.data, fast.data)
                    fast.data = fast.next.data
                    fast.next.data = temp
                    
                    fast = fast.next
                print("    ", slow.data)
                #slow = slow.next

    def sum_lists(self, other):
        sum = 0
        base = 1
        carry = 0
        first = True

        first_list = self.head
        second_list = other.head

        while first_list != None or second_list != None:
            if first_list != None and second_list != None:
                if first_list.data + second_list.data + carry >= 10:
                    first_list.data = first_list.data + second_list.data + carry - 10
                    second_list.data = first_list.data

                    carry = 1
                else:
                    first_list.data = first_list.data + second_list.data + carry
                    second_list.data = first_list.data

                    carry = 0

                first_list = first_list.next
                second_list = second_list.next
            elif first_list != None:
                if first_list.data + carry >= 10:
                    first_list.data = first_list.data + carry - 10

                    carry = 1
                else:
                    first_list.data = first_list.data + carry

                    carry = 0

                first_list = first_list.next
            else:
                first = False
                if second_list.data + carry >= 10:
                    second_list.data = second_list.data  + carry - 10

                    carry = 1
                else:
                    second_list.data = second_list.data + carry

                    carry = 0
                second_list = second_list.next
        if first:
            if carry == 1:
                self.append_to_tail(carry)
            return self
        else:
            if carry == 1:
                other.append_to_tail(carry)
            return other


        return self, other
        #return sum


def main():
    linked_list = LinkedList(1)
    linked_list.append_to_tail(5)
    linked_list.append_to_tail(9)
    #linked_list.append_to_tail(6)
    #linked_list.append_to_tail(10)
    #linked_list.append_to_tail(2)
    #linked_list.append_to_tail(1)
    print(linked_list)

    linked_list2 = LinkedList(2)
    linked_list2.append_to_tail(3)
    linked_list2.append_to_tail(6)
    #linked_list2.append_to_tail(7)
    print(linked_list2)

    L = linked_list.sum_lists(linked_list2)
    print(L)
    print(linked_list)
    print(linked_list2)
    

if __name__ == "__main__":
    main()

        