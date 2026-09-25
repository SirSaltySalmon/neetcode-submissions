class Solution:
    def longestPalindrome(self, s: str) -> str:
        # palindromes can be checked when
        # you start from a center and expand outwards
        # so for n^2...
        # you can pick each center once
        # and expand it out. each expansion is O(n)
        # does n times so O(n^2)
        # let's do recusion!

        def expand(i):
            l = i
            r = i
            cur_size = 1
            # palindrome center either be odd or even len
            # expand left and right by 1s to see the
            # length of the center first.
            while l > 0 and s[l - 1] == s[i]:
                l -= 1
                cur_size += 1
            while r < len(s) - 1 and s[r + 1] == s[i]:
                r += 1
                cur_size += 1
            while (
                l > 0 and r < len(s) - 1 and
                s[l - 1] == s[r + 1]
            ):
                l -= 1
                r += 1
                cur_size += 2
            
            return (cur_size, s[l:r+1])

        max_len = (0, "")
        for i in range(len(s)):
            max_len = max(expand(i), max_len)
        
        return max_len[1]
        