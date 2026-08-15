class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []

        current = []
        number = 0

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)

            elif c == '[':
                count_stack.append(number)
                string_stack.append(current)

                number = 0
                current = []

            elif c == ']':
                repeat_count = count_stack.pop()
                previous = string_stack.pop()

                current = previous + current * repeat_count

            else:
                current.append(c)

        return ''.join(current)