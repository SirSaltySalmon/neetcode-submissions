from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results_hash_map = defaultdict(list)
        for string in strs:
            char_tuple = self.get_char_tuple(string)
            results_hash_map[char_tuple].append(string)
        
        return list(results_hash_map.values())
    
    def get_char_tuple(self, string: str): #Can't use dict as a hashmap
        #Array or list isn't hashable either!
        #But tuple is immutable and likely hashable
        char_array = [0 for i in range(26)]
        for char in string:
            index = ord(char) - ord('a')
            #ord returns unicode value
            char_array[index] += 1
        
        return tuple(char_array)
