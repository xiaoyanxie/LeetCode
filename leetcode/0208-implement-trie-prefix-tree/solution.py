class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
                continue
            curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, c in enumerate(prefix):
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
