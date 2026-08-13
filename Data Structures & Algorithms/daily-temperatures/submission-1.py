class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while (stack != [] and
                    temperatures[i] > temperatures[stack[-1]]
                    ):
            # If the current temperature is higher than the highest in
            # the stack, then it means all the temperatures in the stack
            # now knows what is their next warmer day!!!
                i_to_upd = stack.pop()
                res[i_to_upd] = i - i_to_upd
                # And since it's popped out and processed, it is
                # never touched again. So it's O(n)!!!
            stack.append(i)
        
        return res
            

