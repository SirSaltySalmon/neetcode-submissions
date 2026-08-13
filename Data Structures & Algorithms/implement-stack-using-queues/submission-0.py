import queue

class MyStack:

    queue1: List
    queue2: List

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        # dequeue is equivalent to pop(0)
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        
        # queue1 now only has its last inputted item, which is what we want
        item = self.queue1.pop(0)

        # reconstruct queue1
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        
        return item

    def top(self) -> int:
        # very similar to pop
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.pop(0))
        item = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return item

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()