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

def main():
    linked_list = LinkedList(10)
    linked_list.append_to_tail(12)
    linked_list.append_to_tail(14)
    linked_list.append_to_tail(11)
    linked_list.append_to_tail(14)
    linked_list.append_to_tail(12)
    linked_list.append_to_tail(12)
    linked_list.append_to_tail(14)
    print(linked_list)

    linked_list.remove_dups_no_buffer()
    print(linked_list)

if __name__ == "__main__":
    main()

        