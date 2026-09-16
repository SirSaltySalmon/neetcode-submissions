class TrieNode:
    val: str
    word: bool
    children: dict
    
    def __init__(self, val = ""):
        self.val = val
        self.word = False
        self.children = {}

class WordDictionary:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                new_node = TrieNode(c)
                cur_node.children[c] = new_node
                cur_node = new_node
        cur_node.word = True

    def search(self, word: str) -> bool:
        # use recursion

        def dfs(node, index) -> bool:
            # in this dfs, index is the NEXT letter
            # so below means, if there are no next letter
            # we are at the end!
            if index == len(word):
                return node.word
            
            c = word[index]

            if c != ".":
                if c in node.children:
                    return dfs(node.children[c], index + 1)
                return False
            else:
                for v in node.children.values():
                    if dfs(v, index + 1):
                        return True
                return False
        
        return dfs(self.root, 0)