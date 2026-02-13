class Node:
    def __init__(self, char):
        self.c = char
        self.isWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        if not word:
            return
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
                continue
            curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
                continue
            else:
                return False
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, c in enumerate(prefix):
            if c in curr.children:
                curr = curr.children[c]
                continue
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
