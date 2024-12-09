class Queue:
    def __init__(self):
        self.queue = []
    
    # Enqueue: Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # Dequeue: Remove an element from the front of the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
            return None
        else:
            item = self.queue[0]
            # Manually shift elements to maintain the queue order
            for i in range(1, len(self.queue)):
                self.queue[i - 1] = self.queue[i]
            self.queue.pop()  # Remove the last element, now duplicated
            return item
    
    # Display the queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("Queue:", self.queue)

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0


# Example Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()     # Output: Queue: [10, 20, 30]

print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
q.display()     # Output: Queue: [20, 30]
