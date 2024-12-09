print("Output for Singly Linked List")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    if head is None:
        return Node(data)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(data)
    return head

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def delete_node(head, key):
    if head and head.data == key:
        return head.next
    temp = head
    while temp and temp.next and temp.next.data != key:
        temp = temp.next
    if temp and temp.next:
        temp.next = temp.next.next
    else:
        print(f"Value {key} not found in the list.")
    return head

def display_list(head):
    temp = head
    if not temp:
        print("The list is empty.")
    while temp:
        print(temp.data, end=" -> " if temp.next else " -> None\n")
        temp = temp.next

def menu():
    head = None
    while True:
        choice = input("\n1. Insert at beginning\n2. Insert at end\n3. Delete a node\n4. Display list\n5. Exit\nEnter choice (1-5): ")
        if choice == '1':
            head = insert_at_beginning(head, input("Data to insert at beginning: "))
        elif choice == '2':
            head = insert_at_end(head, input("Data to insert at end: "))
        elif choice == '3':
            head = delete_node(head, input("Value to delete: "))
        elif choice == '4':
            display_list(head)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
