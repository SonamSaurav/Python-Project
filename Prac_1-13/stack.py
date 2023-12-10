# This is for Stack Q8


class Stack:
    def __init__(self):
        self.items = []

    def display(self):
        if not self.is_empty():
            print("Stack:", self.items)
        else:
            print("Stack is empty.")

    def insert(self, item):
        self.items.append(item)
        print(f"{item} has been inserted into the stack.")

    def delete(self):
        if not self.is_empty():
            removed_item = self.items.pop()
            print(f"{removed_item} has been deleted from the stack.")
        else:
            print("Stack is empty. Cannot delete.")

    def is_empty(self):
        return len(self.items) == 0


def main():
    stack = Stack()

    while True:
        print("\nMenu:")
        print("1. Display")
        print("2. Insert")
        print("3. Delete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            stack.display()
        elif choice == '2':
            item = input("Enter the item to insert: ")
            stack.insert(item)
        elif choice == '3':
            stack.delete()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
