#Write a program to create a circular queue using dictionaries in python
#Maximum length of the queue is 5:
#if it crosses the maximum length it has to delete the latest added element in the queue and add the new element to the queue



class CircularQueue:
    def __init__(self, max_length):
        self.queue = {}
        self.max_length = max_length

    def addqueue(self, element)
        if len(self.queue) == self.max_length:
            # Queue is full, remove the last added element
            self.dequeue()

        self.queue[len(self.queue)] = element

    def delqueue(self):
        if not self.queue:
            # Queue is empty
            print("Queue is empty.")
            return None

        removed_element = self.queue.pop(len(self.queue) - 1)
        return removed_element

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Circular Queue:", list(self.queue.values()))


cq = CircularQueue(5)

cq.addqueue(1)
cq.addqueue(2)
cq.addqueue(3)
cq.display()

cq.addqueue(4)
cq.addqueue(5) 
cq.display()

cq.addqueue(6)
cq.display()
