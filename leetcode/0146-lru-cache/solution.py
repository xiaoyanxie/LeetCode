class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def unlink(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToTail(self, node):
        realTail = self.tail.prev
        realTail.next = node
        node.prev = realTail

        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        node.unlink()
        self.addToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.unlink()
            self.addToTail(node)
            return
        
        if len(self.cache) == self.capacity:
            evcit = self.head.next
            evcit.unlink()
            del self.cache[evcit.key]

        node = Node(key, value)
        self.cache[key] = node
        self.addToTail(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
