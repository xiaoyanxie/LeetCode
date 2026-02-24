class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        
        self.nums.append(val)
        self.index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        i = self.index[val]
        self.index[self.nums[-1]] = i
        del self.index[val]

        # swap and pop
        self.nums[i], self.nums[-1] = self.nums[-1], self.nums[i]
        self.nums.pop()
        # print(f'removed {val}, index={self.index}, nums={self.nums}')
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
