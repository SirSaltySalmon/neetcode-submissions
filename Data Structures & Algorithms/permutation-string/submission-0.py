class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_hashmap = {}
        for c in s1:
            val = s1_hashmap.get(c, 0)
            s1_hashmap[c] = val + 1
        
        s2_hashmap = {}
        L = 0
        for R in range(len(s2)):
            val = s2_hashmap.get(s2[R], 0)
            s2_hashmap[s2[R]] = val + 1
            length = R - L + 1
            if length > len(s1):
                s2_hashmap[s2[L]] -= 1
                if s2_hashmap[s2[L]] == 0:
                    del s2_hashmap[s2[L]]
                L += 1
            if s2_hashmap == s1_hashmap:
                return True
        
        return False