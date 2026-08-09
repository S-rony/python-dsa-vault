class MyStack:

    def __init__(self):
        self.qu = []
        self.qu_2 = []
    def push(self, x: int) -> None:
        return self.qu.append(x)
        # return self.qu_2.append()
    def pop(self) -> int:
        if  len(self.qu) == 0 :
            self.qu, self.qu_2 = self.qu_2, self.qu
        while len(self.qu) > 1:
            self.qu_2.append(self.qu.pop(0))
        return self.qu.pop(0)

    def top(self) -> int:
        if len(self.qu) == 0:
            self.qu, self.qu_2 = self.qu_2, self.qu
        while len(self.qu) > 1:
            self.qu_2.append(self.qu.pop(0))
        top_element = self.qu[0]
        self.qu_2.append(self.qu.pop(0))
        while len(self.qu_2) > 0:
            self.qu.append(self.qu_2.pop(0))
        return top_element

    def empty(self) -> bool:
        if len(self.qu) != 0 or len(self.qu_2) != 0:
            return False
        return True
"----------------------------------------------------------"
#one-queue approach











