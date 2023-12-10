# THIS IS FOR DEQUEUE AND ENQUEUE Q10

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} has been enqueued.")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"{removed_item} has been dequeued.")
        else:
            print("Queue is empty. Cannot dequeue.")

    def display(self):
        if not self.is_empty():
            print("Queue:", self.items)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0


def main():
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
