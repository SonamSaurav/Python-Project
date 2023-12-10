

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")
