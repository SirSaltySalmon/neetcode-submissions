class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        max_length = 0
        L = 0
        for R in range(len(s)):
            index_of_last_occurence_of_char = hashmap.get(s[R], -1)
            if index_of_last_occurence_of_char >= L:
                L = index_of_last_occurence_of_char + 1
            hashmap[s[R]] = R
            length = R - L + 1
            max_length = max(max_length, length)
        return max_length
