class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        i = 0
        while i < len(path):
            temp = ''
            if path[i] == '/':
                i += 1
            elif path[i] == '.':
                while i < len(path) and path[i] != '/':
                    temp += path[i]
                    i += 1
                if temp == '.':
                    pass
                elif temp == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(temp)
            else:
                while i < len(path) and path[i] != '/':
                    temp += path[i]
                    i += 1
                stack.append(temp)
        
        # Root directory
        if not stack:
            return '/'
        
        result = ''
        # Now construct the string:
        for directory in stack:
            result += '/' + directory
        return result