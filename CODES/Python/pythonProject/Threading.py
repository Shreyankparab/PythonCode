# Function to print even numbers
def print_even():
    for i in range(2, 11, 2):
        print(f"Even: {i}")

# Function to print odd numbers
def print_odd():
    for i in range(1, 10, 2):
        print(f"Odd: {i}")

# Simulate concurrent execution by alternating function calls
for i in range(1):
    print_odd()
    print_even()
