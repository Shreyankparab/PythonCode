def sum_of_natural_numbers(n):
    # Base case: if n is 1, return 1 (as sum of the first natural number is 1)
    if n == 1:
        return 1
    # Recursive case: n + sum of numbers up to (n - 1)
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage
num = input("Enter a positive integer: ")

# Input validation to ensure num is a positive integer
if num.isdigit() and int(num) > 0:
    num = int(num)
    print(f"The sum of natural numbers up to {num} is {sum_of_natural_numbers(num)}.")
else:
    print("Please enter a valid positive integer.")
