class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next = None
        self.prev = None
    
    def insertLeft(self, node):
        self.prev.next = node
        node.prev = self.prev

        self.prev = node
        node.next = self

class LRUCache:

    def __init__(self, capacity: int):
        """
        "LRUCache", "put", "put",   "get", "put",  "get", "put", "get", "get", "get"
        [2],        [1, 1], [2, 2], [1],   [3, 3], [2],   [4, 4], [1],  [3],   [4]

        size = 2
        cache: {
            1: node(1, 1),
            2: node(2, 2)
        }
        head <-> node(1, 1) <-> tail
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        node.unlink()
        self.tail.insertLeft(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.unlink()
            self.tail.insertLeft(node)
            return

        if len(self.cache) == self.capacity:
            # evcit
            evcit = self.head.next
            evcit.unlink()
            del self.cache[evcit.key]

        node = Node(key, value)
        self.cache[key] = node
        self.tail.insertLeft(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
