class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def enqueue(self,value):
        #full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")

        #empty
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        #one element present or more element present we will increment the rear only
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

        #deleted
    def dequeue(self):
        #Empty
        if(self.front) == -1:
            print("Queue is empty")

        #only one element present in the array
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = - 1

        #more then one element present in the array
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()