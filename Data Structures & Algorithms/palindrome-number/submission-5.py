

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = 0
        num = x
        while num:
            last_digit = num % 10
            reversed_num = reversed_num * 10 + last_digit
            num //= 10
        
        return reversed_num == x
