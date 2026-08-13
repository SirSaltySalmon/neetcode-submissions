class MyStack:

    # 1 queue version
    q: List

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))
        return self.q.pop(0)

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))
        item = self.q[0]
        self.q.append(self.q.pop(0))
        return item

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()