# THIS IS FOR SECOND QUESTION


def create_array():
    try:
        # Get the length of the array from the user
        length = int(input("Enter the length of the array: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return

        # Initialize an empty array
        user_array = []

        # Input elements from the user
        for i in range(length):
            element = input(f"Enter element {i + 1}: ")
            user_array.append(element)

        # Display the created array
        print("\nArray created:")
        print(user_array)

    except ValueError:
        print("Please enter a valid integer for the length.")


# Example usage:
if __name__ == "__main__":
    create_array()

