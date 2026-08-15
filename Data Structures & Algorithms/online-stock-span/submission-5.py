class StockSpanner:
    stack: List

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        else:
            span = 1
            while self.stack and price >= self.stack[-1][0]:
                # Since if the next price comes in and is smaller than this price,
                # It's span will be blocked by this price and becomes 1 anyway
                # So it doesn't matter that we're omitting information that could be
                # contribute to the span, because it won't
                pair = self.stack.pop()
                span += pair[1]
            self.stack.append((price, span))
            return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)