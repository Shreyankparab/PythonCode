print("Output for Doubly Linked List")

# Node of a Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next, new_node.prev = new_node, temp
        print(f"Inserted {data} at the end.")

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next, self.head.prev = self.head, new_node
            self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def delete_node(self, data):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return

        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        if not temp:
            print(f"Element {data} not found in the list.")
        else:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            if temp == self.head:
                self.head = temp.next
            print(f"Deleted {data} from the list.")

    def display_forward(self):
        temp = self.head
        if not temp:
            print("List is empty.")
        else:
            print("Forward: ", end="")
            while temp:
                print(temp.data, end=" <-> " if temp.next else "\n")
                temp = temp.next

    def display_backward(self):
        temp = self.head
        if not temp:
            print("List is empty.")
        else:
            while temp.next:
                temp = temp.next
            print("Backward: ", end="")
            while temp:
                print(temp.data, end=" <-> " if temp.prev else "\n")
                temp = temp.prev

# Main menu-driven function
def menu():
    dll = DoublyLinkedList()
    while True:
        choice = input("\n1. Insert at Beginning\n2. Insert at End\n3. Delete a Node\n4. Display Forward\n5. Display Backward\n6. Exit\nEnter your choice (1-6): ")
        if choice == '1':
            dll.insert_beginning(input("Enter the element: "))
        elif choice == '2':
            dll.insert_end(input("Enter the element: "))
        elif choice == '3':
            dll.delete_node(input("Enter the element to delete: "))
        elif choice == '4':
            dll.display_forward()
        elif choice == '5':
            dll.display_backward()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
