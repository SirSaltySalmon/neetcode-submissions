class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        cur = []

        def backtrack(i):
            if i >= len(digits):
                if cur:
                    res.append("".join(cur))
                return
            
            chars = num_to_char[digits[i]]
            for c in chars:
                cur.append(c)
                backtrack(i+1)
                cur.pop()
        
        backtrack(0)
        return res