class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert_at_end(self, value):
        self.items.append(value)

    def delete_at_beg(self):
        if self.is_empty():
            return "Deque is Empty"
        else:
            return self.items.pop(0)

    def insert_at_beg(self,value):
        self.items.insert(0,value)

    def delete_at_end(self):
        if self.is_empty():
            return "Deque is Empty"
        return self.items.pop()

deq = Deque()
deq.insert_at_beg(10)
deq.insert_at_end(20)
deq.insert_at_beg(5)
deq.insert_at_end(30)

print(deq.delete_at_beg())
print(deq.delete_at_end())
print(deq.delete_at_end())
print(deq.delete_at_beg())




