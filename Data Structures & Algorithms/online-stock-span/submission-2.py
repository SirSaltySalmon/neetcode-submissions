class StockSpanner:
    stack: List

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        else:
            count = 0
            self.stack.append(price)
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i] <= price:
                    count += 1
                else:
                    break
            return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)