class Solution:
    def countSubstrings(self, s: str) -> int:
        # idea...
        # as you expand out you also count
        # but this risk you counting the same thing twice
        # use hash set to make sure u dont repeat?
        # sure, if you save the pointers
        # see but this is O(n^3) and O(n^2) space
        # lot of repeated work is done in isPalindrome
        # so we just gonna remove that function

        count = 0

        def expand(i, i2):
            nonlocal count

            l = i
            r = i2
            
            while (l >= 0) and (r < len(s)):
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return count