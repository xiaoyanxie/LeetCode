from collections import deque, defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # ["wrt","wrf","er","ett","rftt"]
        # t->f, w->e, r->t, e->r
        # return "wertf"

        # ["abcd", "abcde"]
        # a, b, c, d, e
        # return "abcde" or "aebcd"

        # ["abcde", "abcd"]
        # return ""

        # ["w", "t", "z", "w"]
        # w->t, t->z, z->w
        # return ""

        indegree = {char: 0 for word in words for char in word}
        graph = defaultdict(set)
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

        queue = deque([ char for char in indegree if indegree[char] == 0 ])
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(indegree) != len(result):
            return ""

        return "".join(result)
