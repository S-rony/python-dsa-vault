class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def enqueue(self,value):
        if self.is_full():
            return
        elif self.is_empty():
            self.rear = self.front = 0
            self.items[self.rear] = value

        else:
            self.rear = (self.rear+1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            return
        elif self.rear == self.front:
            self.front = self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

    def front(self):
        return self.items[self.front]

    def is_empty(self):
        if self.front == -1:
            return True
        return False

    def is_full(self):
        if (self.rear+1) % self.size == self.front:
            return True
        else:
            return False


