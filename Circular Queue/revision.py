class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1
    #isertion of the element
    def enqueue(self, value):
        #Full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")

        #Empty
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value

        #one element or more then one element present in the array
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    #deletation of the element
    def dequeue(self):
        #Empty
        if self.front == -1:
            print("Queue is Empty")

        #one stack in the queue
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = -1
        else:
            print(self.items[self.front])
            self.front = (self.front+1) % self.size