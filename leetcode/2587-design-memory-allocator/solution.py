from collections import defaultdict
class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.mp = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        """
        1,1,1,0,0,0
                  i
        length: 2
        """
        i = 0
        length = 0
        while i < len(self.mem):
            allocID = self.mem[i]
            i += 1
            if allocID != 0:
                length = 0
                continue
            
            length += 1
            if length == size:
                break
        else:
            return -1

        i -= length
        self.mem[i:i+size] = [mID] * size
        self.mp[mID].append((i, size))
        return i

    def freeMemory(self, mID: int) -> int:
        if mID not in self.mp:
            return 0

        total = 0
        for start, size in self.mp[mID]:
            self.mem[start:start+size] = [0] * size
            total += size
        del self.mp[mID]
        return total

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
