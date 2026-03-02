from collections import deque
class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.n = n
        """
        []
        pos
        """

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[self.n - idKey] = value
        ret = []
        while self.stream and self.stream[-1] != None:
            ret.append(self.stream.pop())
        return ret

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
