class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        1. exact match
        2. case insensetive match
        3. vowel insensetive match
        """
        original = set()
        caseInsensetive = {}
        vowelInsensetive = {}
        vowels = set(('a', 'e', 'i', 'o', 'u'))

        def devowel(word):
            return ''.join([
                c if c not in vowels else '*' for c in word.lower()
            ])

        for word in wordlist:
            original.add(word)
            lower = word.lower()
            devoweled = devowel(word)
            if lower not in caseInsensetive:
                caseInsensetive[lower] = word
            if devoweled not in vowelInsensetive:
                vowelInsensetive[devoweled] = word
        
        ret = []
        for query in queries:
            lower = query.lower()
            devoweled = devowel(query)

            if query in original:
                ret.append(query)
            elif lower in caseInsensetive:
                ret.append(caseInsensetive[lower])
            elif devoweled in vowelInsensetive:
                ret.append(vowelInsensetive[devoweled])
            else:
                ret.append('')
        return ret
