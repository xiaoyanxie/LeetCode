from sortedcontainers import SortedList
from collections import defaultdict
class Leaderboard:

    def __init__(self):
        """
        Space: O(N)
        """
        self.scores = SortedList()
        self.playerScores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        """
        Time: O(log(N))
        """
        originalScore = self.playerScores[playerId]
        if originalScore > 0:
            self.scores.remove(originalScore)

        self.playerScores[playerId] += score
        self.scores.add(self.playerScores[playerId])

    def top(self, K: int) -> int:
        """
        Time: O(log(N) + K)
        """
        return sum(self.scores[-K:])

    def reset(self, playerId: int) -> None:
        """
        Time: O(log(N))
        """
        originalScore = self.playerScores[playerId]
        self.playerScores[playerId] = 0
        if originalScore > 0:
            self.scores.remove(originalScore)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
