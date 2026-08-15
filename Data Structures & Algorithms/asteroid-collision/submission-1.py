import numpy as np

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        stack = []
        while i < len(asteroids):
            if (stack and stack[-1] > 0 and asteroids[i] < 0):
                # Case 1: Current asteroid will smash the last asteroid
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                    # Continue to compare current asteroid i with new stack top
                # Case 2: Both explode
                elif abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    i += 1
                # Case 3: Last asteroid will smash current asteroid
                else:
                    i += 1
            else:
                stack.append(asteroids[i])
                i += 1
        
        return stack