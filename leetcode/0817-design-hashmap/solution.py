class MyHashMap:

    def __init__(self):
        self.capacity = 100
        self.index = [ [] for _ in range(self.capacity) ]
        self.size = 0

    def __put(self, key, value, capacity, index):
        chain = index[key % capacity]
        for i, kv in enumerate(chain):
            if kv[0] == key:
                kv[1] = value
                return
        chain.append([key, value])
        self.size += 1

    def __ensureCapacity(self):
        if self.size < self.capacity * 1.5:
            return
        
        newCapacity = self.capacity * 3
        newIndex = [ [] for _ in range(newCapacity) ]
        self.size = 0
        for chain in self.index:
            for k, v in chain:
                self.__put(k, v, newCapacity, newIndex)
        
        self.capacity = newCapacity
        self.index = newIndex

    def put(self, key: int, value: int) -> None:
        self.__ensureCapacity()
        self.__put(key, value, self.capacity, self.index)

    def get(self, key: int) -> int:
        chain = self.index[key % self.capacity]
        for i, kv in enumerate(chain):
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        chain = self.index[key % self.capacity]
        for i, kv in enumerate(chain):
            if kv[0] == key:
                chain[i], chain[-1] = chain[-1], chain[i]
                chain.pop()
                self.size -= 1
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
