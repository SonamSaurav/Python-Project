# This is for Stack using Linked List Q9


# (i) Linear Search Algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# (ii) Binary Search Algorithm (Assumes the array is sorted)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

#  usage
arr = [2, 5, 8, 12, 16, 23, 38, 42, 55, 67]
target_value = int(input("Enter the target value to search: "))

# Linear Search
linear_search_result = linear_search(arr, target_value)
if linear_search_result != -1:
    print(f"Linear Search: Target found at index {linear_search_result}")
else:
    print("Linear Search: Target not found in the array")

# Binary Search (Array should be sorted)
sorted_arr = sorted(arr)
binary_search_result = binary_search(sorted_arr, target_value)
if binary_search_result != -1:
    print(f"Binary Search: Target found at index {binary_search_result}")
else:
    print("Binary Search: Target not found in the sorted array")
