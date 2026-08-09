#LIFO

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, value):
        self.items.append(value)

    def delete(self):
        if self.is_empty():
            return "Queue is Empty"
        else:
            return self.items.pop(0)


que = Queue()
que.insert(10)
que.insert(20)
que.insert(30)
que.insert(40)

print(que.delete())
print(que.delete())
