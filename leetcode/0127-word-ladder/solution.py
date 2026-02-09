class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList:
            return 0
        wordListSet = set(wordList)
        graph = defaultdict(list)
        
        #hit: *it, h*t, hi* : value:hit
        for word in wordListSet:
            for i in range(len(word)):
                transform = f"{word[:i]}*{word[i+1:]}"
                graph[transform].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set(beginWord)

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            
            visited.add(word)
            for i in range(len(word)):
                trans = f"{word[:i]}*{word[i+1:]}"
                # potentials = graph.get(trans, None)
                if trans in graph:
                    for potential in graph[trans]:
                    
                        if potential not in visited:
                            q.append((potential, step + 1))
        
        return 0

            


                
        
