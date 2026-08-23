class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_hashmap = {}
        s_hashmap = {}

        for c in t:
            val = t_hashmap.get(c, 0) + 1
            t_hashmap[c] = val
        
        have = 0
        need = len(t_hashmap)
        
        min_length = float("inf")
        res = (-1, -1)
        L = 0
        for R in range(len(s)):
            val = s_hashmap.get(s[R], 0) + 1
            s_hashmap[s[R]] = val

            val_in_t = t_hashmap.get(s[R], 0)
            if val == val_in_t:
                have += 1
            
            while have == need:
                if (R - L + 1) < min_length:
                    min_length = (R - L + 1)
                    res = (L, R)
                
                val_at_t = t_hashmap.get(s[L], 0)
                if s_hashmap[s[L]] == val_at_t:
                    have -= 1
                s_hashmap[s[L]] -= 1
                L += 1

        if res == (-1, -1):
            return ""
        else:
            L = res[0]
            R = res[1]
            return s[L:R+1]
                        
        