class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create a simple circular doubly linked list
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = head  # Circular link
head.prev = third  # Circular link

# Traversing the circular doubly linked list forward
temp = head
for _ in range(6):  # Loop multiple times to show circular nature
    print(temp.data, end=" -> ")
    temp = temp.next

# Output: 10 -> 20 -> 30 -> 10 -> 20 -> 30 ->
