class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.is_last = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_last = True
            
    def search(self, word: str) -> bool:
        root = self.trie
        def find(node, idx): #(g,3 )
            if idx == len(word): # idx = 3
                return node.is_last
            
            c = word[idx] # c = g
            if c != ".":
                if c in node.children:
                    return find(node.children[c], idx + 1)
                else:
                    return False
            
            # c = a - z
            for char in node.children: 
                found = find(node.children[char], idx + 1)#b,c,d
                if found:
                    return True
            return False

        return find(root, 0)
"""
        dummy
          |
          a
        | | |
        b c d
        |   |
        e   g
word = a.g
dfs(dummy, 0) ->dfs(node(a), 1) -> dfs(node(b), 2) -> False
                                -> dfs(node(c), 2) -> False
                                -> dfs(node(d), 2) -> dfs(node(g), 3) -> is_last -> True

"""        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
