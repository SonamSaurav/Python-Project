class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # (i) Traversing
    def traverse(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    # (ii) Insertion
    # (i) At the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    # (ii) At the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # (iii) Deletion
    # (i) At the beginning
    def delete_at_beginning(self):
        if not self.head:
            print("Circular Linked List is empty. Deletion not possible.")
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    # (ii) At the end
    def delete_at_end(self):
        if not self.head:
            print("Circular Linked List is empty. Deletion not possible.")
            return
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head

# Example usage
circular_list = CircularLinkedList()

circular_list.insert_at_beginning(3)
circular_list.insert_at_beginning(2)
circular_list.insert_at_beginning(1)

circular_list.traverse()

circular_list.insert_at_end(4)
circular_list.insert_at_end(5)

circular_list.traverse()

circular_list.delete_at_beginning()
circular_list.traverse()

circular_list.delete_at_end()
circular_list.traverse()
