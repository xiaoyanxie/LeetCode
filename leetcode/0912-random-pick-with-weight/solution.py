class Solution:

    def __init__(self, w: List[int]):
        self.numbers = []
        self.size = 0
        for num, weight in enumerate(w):
            self.size += weight
            if num == 0:
                self.numbers.append((num, weight - 1))
            else:
                start = self.numbers[-1][1] + 1
                self.numbers.append((num, start + weight - 1))

    def pickIndex(self) -> int:
        i = random.randint(0, self.size - 1)
        j = bisect.bisect_left(self.numbers, i, key=lambda x: x[1])
        return self.numbers[j][0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
