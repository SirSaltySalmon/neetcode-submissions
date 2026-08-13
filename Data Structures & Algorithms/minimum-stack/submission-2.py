class MinStack:
    s: List
    min_s: List

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        ## The min_s only updates if the given element is a new minimum
        if not self.min_s or val <= self.min_s[-1]:
            self.min_s.append(val)

    def pop(self) -> None:
        if not self.s:
            return None
        val = self.s.pop()
        if val == self.min_s[-1]:
            self.min_s.pop()
        
    def top(self) -> int:
        if not self.s:
            return None
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]