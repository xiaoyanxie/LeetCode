class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        1. lookup the set(wordList), if a match, add to result

        2. lookup the case insensitive map, if a match, return the first match in the wordlist: for example: HARE matches hare -> [hare, Hare], then return hare

        3. mask the vowel, lookup the masked vowel map, if there is a match, return the first match like 2)
        """

        original = set(wordlist)
        caseInsensitive = {}
        deVowels = {}

        def deVowel(w):
            ret = []
            for c in w:
                if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                    ret.append('*')
                else:
                    ret.append(c.lower())
            return ''.join(ret)

        for w in wordlist:
            w0 = w.lower()
            if w0 not in caseInsensitive:
                caseInsensitive[w0] = w
            w1 = deVowel(w)
            if w1 not in deVowels:
                deVowels[w1] = w
        
        ret = []
        for query in queries:
            if query in original:
                ret.append(query)
            elif query.lower() in caseInsensitive:
                ret.append(caseInsensitive[query.lower()])
            else:
                w = deVowel(query)
                if w in deVowels:
                    ret.append(deVowels[w])
                else:
                    ret.append('')
        return ret
