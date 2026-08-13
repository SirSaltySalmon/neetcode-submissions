class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{','[']:
                stack.append(char)
            elif char in [')','}',']']:
                if stack == []:
                    return False
                opening = stack.pop()
                if opening == '(' and char != ')':
                    return False
                if opening == '{' and char != '}':
                    return False
                if opening == '[' and char != ']':
                    return False
        
        if stack != []:
            return False
        
        return True