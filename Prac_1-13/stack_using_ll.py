# This is for Stack using Linked List Q9


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def display_stack(self):
        if not self.top:
            print("Stack is empty.")
        else:
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print()

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Element {data} pushed onto the stack.")

    def pop(self):
        if not self.top:
            print("Stack is empty. Cannot pop.")
        else:
            popped_element = self.top.data
            self.top = self.top.next
            print(f"Element {popped_element} popped from the stack.")

# Example usage
stack_linked_list = StackLinkedList()

while True:
    print("\nChoose operation:")
    print("1. Display Stack")
    print("2. Insert (Push) Element")
    print("3. Delete (Pop) Element")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        stack_linked_list.display_stack()
    elif choice == '2':
        element = int(input("Enter element to push onto the stack: "))
        stack_linked_list.push(element)
    elif choice == '3':
        stack_linked_list.pop()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
