class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        memo = {}

        def helper(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            inner_len = helper(l + 1, r - 1)
            if s[l] == s[r]:
                if l == r:
                    res = 1 + inner_len
                    memo[(l, r)] = res
                    return res
                else:
                    res = 2 + inner_len
                    memo[(l, r)] = res
                    return res
            else:
                res = max(helper(l + 1, r), helper(l, r - 1))
                memo[(l, r)] = res
                return res

        return helper(0, len(s) - 1)
        