class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a simple circular linked list
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head  # Circular link

# Traversing the circular list
temp = head
for _ in range(6):  # Loop multiple times to show circular nature
    print(temp.data, end=" -> ")
    temp = temp.next

# Output: 10 -> 20 -> 30 -> 10 -> 20 -> 30 ->
