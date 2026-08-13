import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                number1 = stack.pop()
                number2 = stack.pop() # Earlier number
                if tokens[i] == '+':
                    stack.append(number2 + number1)
                elif tokens[i] == '-':
                    stack.append(number2 - number1)
                elif tokens[i] == '*':
                    stack.append(number2 * number1)
                elif tokens[i] == '/':
                    res = number2 / number1
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                    stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()