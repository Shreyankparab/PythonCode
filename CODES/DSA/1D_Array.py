def display_menu():
    print("\nMenu:")
    print("1. Add Element")
    print("2. Remove Element")
    print("3. Display Array")
    print("4. Search Element")
    print("5. Exit")

def add_element(arr):
    element = input("Enter the element to add: ")
    # Manually resizing the array (simple approach)
    arr.append(None)  # Add a placeholder to extend the array
    i = len(arr) - 1  # Get the last index
    while i > 0:
        arr[i] = arr[i - 1]  # Shift elements to the right
        i -= 1
    arr[0] = element  # Add new element at the beginning
    print(f"Element '{element}' added.")

def remove_element(arr):
    element = input("Enter the element to remove: ")
    found = False
    for i in range(len(arr)):
        if arr[i] == element:
            found = True
            # Shift elements to the left to remove the element
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()  # Remove the last element (which is now a duplicate)
            print(f"Element '{element}' removed.")
            break
    if not found:
        print(f"Element '{element}' not found in the array.")

def display_array(arr):
    if len(arr) > 0:
        print("Current Array:", end=' ')
        for element in arr:
            print(element, end=' ')
        print()  # New line
    else:
        print("The array is empty.")

def search_element(arr):
    element = input("Enter the element to search for: ")
    found = False
    for i in range(len(arr)):
        if arr[i] == element:
            found = True
            print(f"Element '{element}' found at index {i}.")
            break
    if not found:
        print(f"Element '{element}' not found in the array.")

def main():
    arr = []
    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_element(arr)
        elif choice == '2':
            remove_element(arr)
        elif choice == '3':
            display_array(arr)
        elif choice == '4':
            search_element(arr)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
