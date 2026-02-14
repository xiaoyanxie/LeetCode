class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        count = 0
        digit = []
        while i < len(abbr) and j < len(word):
            if abbr[i].isalpha():
                if abbr[i] == word[j]:
                    i+=1
                    j+=1
                    continue
                else:
                    return False
            elif abbr[i] == '0':
                return False
            elif abbr[i].isdigit():
                sum = 0
                while i < len(abbr) and abbr[i].isdigit():
                    sum = sum * 10 + int(abbr[i])
                    i+=1
                j+= sum
                continue
            else:
                return False   
            
        return i == len(abbr) and j == len(word)
            
