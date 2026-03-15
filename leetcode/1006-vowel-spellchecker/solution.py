class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = [''] * len(queries)
        strictList = set()
        caseInsensitiveList = {}
        vowelInsensitiveList = {}

        def removeVowels(word):
            ret = []
            for c in word.lower():
                if c in 'aeiou':
                    ret.append('*')
                else:
                    ret.append(c)
            return ''.join(ret)

        for word in wordlist:
            strictList.add(word)
            if word.lower() not in caseInsensitiveList:
                caseInsensitiveList[word.lower()] = word
            devowel = removeVowels(word)
            if devowel not in vowelInsensitiveList:
                vowelInsensitiveList[devowel] = word
        
        """
        "KiTe","kite","hare","Hare"

        strictList: {"KiTe","kite","hare","Hare"}
        caseInsensitiveList: {
            'kite': 'KiTe',
            'hare': 'hare'
        }
        vowelInsensitiveList: {
            'k*t*': 'KiTe',
            'h*r*': 'hare'
        }

        "kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"
                
         kite   KiTe   KiTe   Hare   hare   ''     ''     KiTe   ''     KiTe
        """

        for i, query in enumerate(queries):
            """
            Precedence Rules:
            0. Strict match
            1. Case-insensitive: what happens if 'abc' -> ['aBc', 'Abc'], return 'aBc'
            2. Vowel Errors: what happens if 'y*ll*w' -> ['YellOw', 'Yellow'], return 'YellOw'
            3. No match: return empty string
            """
            if query in strictList:
                answer[i] = query
            elif query.lower() in caseInsensitiveList:
                answer[i] = caseInsensitiveList[query.lower()]
            else:
                devowel = removeVowels(query)
                if devowel in vowelInsensitiveList:
                    answer[i] = vowelInsensitiveList[devowel]
        
        return answer
