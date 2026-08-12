class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for string in strs:
            chunk = str(len(string)) + "#" + string
            encoded_str += chunk
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_to_parse = int(s[i:j])
            i = j + 1 # Skip separator
            decoded_strs.append(s[i : i + length_to_parse])
            i += length_to_parse # Get to the start of the next encoded length
        return decoded_strs