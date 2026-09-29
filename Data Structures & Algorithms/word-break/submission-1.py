class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # add characters until it matches a word
        # when it does, break there, and keep going down another branch
        # 1. let's make wordDict a hash set for O(1) lookup
        # 2. add memoization

        setDict = set(wordDict)
        badIndexes = set()

        def helper(i):
            if i == len(s):
                return True
            if i in badIndexes:
                return False
            word = ""
            for j in range(i, len(s)):
                word += s[j]
                if word in setDict:
                    if helper(j + 1):
                        return True
            badIndexes.add(i)
            return False
        
        return helper(0)
            