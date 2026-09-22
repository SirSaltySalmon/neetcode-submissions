# idea: find start, look in all directions except last
# use hashset to keep track of visited
# found then quit
# complexity? m * n for finding first letter
# * 3^t where t is word length as must travel 3 directions minimum
# + s for the hashset size

# ... works, but is too inefficient apparently.
# The complexity I calculated is true for a single word.... I didn't think
# For many words, I am still doing dfs all over the place again
# Why not do one dfs for many words with same prefixes?
# ...which is crazy by the way.
# I would have never been able to fucking think of that shit.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res = set()
        visited = set()
        
        def searchWord(node, row, col, word):
            if not (0 <= row and row < len(board)):
                return False
            if not (0 <= col and col < len(board[i])):
                return False
            if (row, col) in visited:
                return False
            #... and, if the letter isn't in the search at all......
            c = board[row][col]
            if not c in node.children:
                return False
            
            visited.add((row,col))
            node = node.children[c]
            word += c
            if node.isWord:
                res.add(word)

            searchWord(node, row + 1, col, word)
            searchWord(node, row - 1, col, word)
            searchWord(node, row, col + 1, word)
            searchWord(node, row, col - 1, word)
            visited.remove((row, col))
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                searchWord(root, i, j, "")
        
        return list(res)