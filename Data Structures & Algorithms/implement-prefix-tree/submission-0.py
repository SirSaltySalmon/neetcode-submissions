class TrieNode:
    val: str
    word: bool
    children: dict

    def __init__(self, val = "", word = False):
        self.val = val
        self.word = word
        self.children = {}

class PrefixTree:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
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
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return cur_node.word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return False
        return True
        