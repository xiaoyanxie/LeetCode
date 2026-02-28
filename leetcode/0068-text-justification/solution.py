class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        processing = []
        current = []
        remainingWidth = maxWidth
        spaces = 0
        for i, word in enumerate(words):
            if current and len(word) >= remainingWidth:
                processing.append((current, remainingWidth, spaces, len(processing)))
                current = []
                remainingWidth = maxWidth
                spaces = 0
            if not current:
                current.append(word)
                remainingWidth -= len(word)
            elif len(word) < remainingWidth:
                current.append(' ')
                current.append(word)
                remainingWidth -= (len(word) + 1)
                spaces += 1
        
        if current:
            processing.append((current, remainingWidth, spaces, len(processing)))
        # print(processing)

        def justify(remainingWidth, spaces):
            return math.ceil(remainingWidth / spaces) * ' '

        ret = []
        for line, remainingWidth, spaces, lineNum in processing:
            # print(processing[lineNum])
            if lineNum == len(processing) - 1 or spaces == 0:
                # left-justified
                ret.append(''.join(line) + remainingWidth * ' ')
            else:
                # fully-justified
                justifiedLine = ''
                for word in line:
                    if word != ' ':
                        justifiedLine += word
                    else:
                        newSpace = justify(remainingWidth, spaces)
                        justifiedLine += (word + newSpace)
                        remainingWidth -= len(newSpace)
                        spaces -= 1
                ret.append(justifiedLine)
        return ret
