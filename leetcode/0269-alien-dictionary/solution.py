from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # ["wrt","wrf","er","ett","rftt"]
        # t->f, w->e, r->t, e->r
        # wertf

        # "abcd", "abcde"
        # return "abcde" or "acbde"

        # "abcde", "abcd"
        # return ""

        # ["a","z","x","z"]
        # build dependencies, indegree map
        indegree = {char: 0 for word in words for char in word} # {z: 1, x: 1, a:0}
        graph = defaultdict(set) # {z: (x), x: (z), a:(z)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        # topsort
        queue = deque([ char for char in indegree if indegree[char] == 0 ]) # [a]
        result = [] # [a]
        while queue:
            char = queue.popleft() # a
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != len(indegree):
            return ""
        return "".join(result)
