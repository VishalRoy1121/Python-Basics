# WAP in python with OOP concept to impliment a user defined queue data structure then perform insert and remove methods with a set of elements. (without pre-defined functions)
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.dequeue())  # Output: 3
