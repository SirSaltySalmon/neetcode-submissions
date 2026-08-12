class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results_hash_map = {}
        for string in strs:
            char_dict = self.get_char_tuple(string)
            if char_dict in results_hash_map:
                results_hash_map[char_dict].append(string)
            else:
                results_hash_map[char_dict] = [string]
        
        results = []
        for key in results_hash_map:
            results.append(results_hash_map[key])
        return results
    
    def get_char_tuple(self, string: str): #Can't use dict as a hashmap
        #Array or list isn't hashable either!
        #But tuple is immutable and likely hashable
        char_array = [0 for i in range(26)]
        for char in string:
            index = ord(char) - ord('a')
            #ord returns unicode value
            char_array[index] += 1
        
        return tuple(char_array)
