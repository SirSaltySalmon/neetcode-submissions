class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def isPalindrome(string):
            for i in range(len(string) // 2):
                if string[i] != string[-i - 1]:
                    return False
            return True

        def backtrack(i):
            if i == len(s):
                res.append(cur.copy())
                return            

            for j in range(i+1, len(s)+1):
                partition = s[i:j]
                if isPalindrome(partition):
                    cur.append(partition)
                    backtrack(j)
                    cur.pop()
            
        backtrack(0)
        return res
        