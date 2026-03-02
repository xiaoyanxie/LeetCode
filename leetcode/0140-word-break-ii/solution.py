class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        ["cat","cats","and","sand","dog"]

        cat -> sand -> dog
        cats -> and -> dog


        catsanddog
                  i
        """
        dictionary = set(wordDict)

        ret = [] # [cat, sand, dog], [cats, and, dog]
        def collect(start, acc) -> list: # i, [cats, and, dog]
            # print(f'search {s[start:]}')
            if start == len(s):
                ret.append(' '.join(acc))
            for i in range(start, len(s) + 1):
                word = s[start:i]
                if s[start:i] in dictionary:
                    # print(f'found {word}')
                    collect(i, acc + [word])
        
        collect(0, [])
        return ret
