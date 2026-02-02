class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True
    
        @cache
        def find(i) -> bool:
            # if i == len(s):
            #     return True
            
            node = root
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_word and (j == len(s) - 1 or find(j + 1)):
                    return True
            return False

        return find(0)
