class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for op in operations:
            if op == '+':
                results.append(results[-1] + results[-2])
            elif op == 'D':
                results.append(results[-1]*2)
            elif op == 'C':
                results.pop()
            else:
                score = int(op)
                results.append(score)
        
        return sum(results)