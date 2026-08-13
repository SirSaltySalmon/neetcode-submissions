class MyStack:
    queue1: List # The empty one
    queue2: List # The stack
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
            # queue2 is already in stack order
        self.queue2 = self.queue1
        self.queue1 = []

    def pop(self) -> int:
        return self.queue2.pop(0)
        
    def top(self) -> int:
        return self.queue2[0]

    def empty(self) -> bool:
        return not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()