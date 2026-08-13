class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        score = 0
        for op in operations:
            if op == '+':
                num_score = results[-1] + results[-2]
                results.append(num_score)
                score += num_score 
            elif op == 'D':
                num_score = results[-1]*2
                results.append(num_score)
                score += num_score
            elif op == 'C':
                to_remove = results.pop()
                score -= to_remove
            else:
                num_score = int(op)
                results.append(num_score)
                score += num_score
        
        return score