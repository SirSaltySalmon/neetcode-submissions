class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        common_prefix = []
        for i in range(len(strs[0])):
            c = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != c:
                    return "".join(common_prefix)
            common_prefix.append(c)
        return "".join(common_prefix)