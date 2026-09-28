class Solution:
    def numDecodings(self, s: str) -> int:
        # well each int is either one digit or two
        # and if the subsequents digits after one repeats
        # then you can paste the same result
        # so a memo works great

        memo = {}

        def helper(i):
            # 1 digit and 2 digit cases
            # if both 2 digit and 1 digit: branches off
            # if only 1 digit: doesn't branch
            # if no cases (leading 0): terminate early

            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            res = 0
            if i in memo:
                return memo[i]
            
            if i + 1 < len(s):
                digits = int(s[i:i+2])
                if digits <= 26:
                    res += helper(i + 2)
            if i < len(s):
                res += helper(i + 1)

            memo[i] = res
            return res
        
        return helper(0)