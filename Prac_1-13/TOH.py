def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary using target as auxiliary
        tower_of_hanoi(n - 1, source, target, auxiliary)
        
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        
        # Move the n-1 disks from auxiliary to target using source as auxiliary
        tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
number_of_disks = int(input("Enter the number of disks for Tower of Hanoi: "))
tower_of_hanoi(number_of_disks, 'A', 'B', 'C')
