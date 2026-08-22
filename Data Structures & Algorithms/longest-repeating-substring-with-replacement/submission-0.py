class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        max_length = 0
        max_frequency = 0
        L = 0
        for R in range(len(s)):
            char_count = hashmap.get(s[R], 0) + 1
            hashmap[s[R]] = char_count
            max_frequency = max(max_frequency, hashmap[s[R]])
            length = R - L + 1
            need_to_replace = length - max_frequency
            while need_to_replace > k:
                hashmap[s[L]] -= 1
                L += 1
                length = R - L + 1
                need_to_replace = length - max_frequency
            max_length = max(length, max_length)
        return max_length