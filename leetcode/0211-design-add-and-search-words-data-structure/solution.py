class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.is_last = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("#")

    def addWord(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.is_last = True

    def search(self, word: str) -> bool:
        """
        dummy
          |
          a
        | | |
        c b d
        |   |
        d   e

        query: a.e

        dfs(dummy, 0) -> dfs(node(a), 1) -> dfs(node(c), 2) -> False
                                         -> dfs(node(b), 2) -> False
                                         -> dfs(node(d), 2) -> dfs(node(e), 3) -> True
        """
        def dfs(root, idx): # node(e), 3
            if idx == len(word):
                return root.is_last

            c = word[idx] # e

            # 1. char is a-z
            if c != '.':
                if c not in root.children:
                    return False
                return dfs(root.children[c], idx + 1)
            
            # 2. char is .
            for char in root.children: # c b [d]
                nxt = root.children[char] # [d]
                found = dfs(nxt, idx + 1)
                if found:
                    return True
            return False
        return dfs(self.trie, 0)

    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
