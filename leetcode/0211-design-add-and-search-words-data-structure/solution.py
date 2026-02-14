class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
                continue
            curr.children[c] = Node()
            curr = curr.children[c]
        curr.isWord = True

    def __search(self, word, i, children):
        if word[i] == '.':
            if i == len(word) - 1:
                # check if there is any words in children
                for k in children:
                    if children[k].isWord:
                        return True
                return False
            else:
                # return true if any child matches the next char
                for k in children:
                    if self.__search(word, i + 1, children[k].children):
                        return True
                return False
        elif word[i] in children:
            node = children[word[i]]
            if i == len(word) - 1:
                return node.isWord
            return self.__search(word, i + 1, node.children)
        return False

    def search(self, word: str) -> bool:
        if not word:
            return True
        return self.__search(word, 0, self.root.children)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
