class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_dict = {}
        for char in s:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
        
        for char in t:
            if not char in chars_dict:
                return False
            
            chars_dict[char] -= 1
        
        for key in chars_dict.keys():
            if chars_dict[key] != 0:
                return False
        
        return True