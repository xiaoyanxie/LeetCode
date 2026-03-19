class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev

        self.prev = None
        self.next = None

    def insertLeft(self, node):
        self.prev.next = node
        node.prev = self.prev

        self.prev = node
        node.next = self

    def toStr(self) -> str:
        s = ''
        curr = self
        while curr:
            s += f'node({curr.key},{curr.val}) <-> '
            curr = curr.next
        return s

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f'get({key})')
        if key not in self.cache:
            return -1
        
        # update access
        node = self.cache[key]
        node.unlink()
        self.tail.insertLeft(node)
        # print(self.head.toStr())
        return node.val

    """
    cap: 2
    index: {
        1 -> node(1,1),
        2 -> node(2,2)
    }
    head <-> node(1,1) <-> node(2,2) <-> tail
    """
    def put(self, key: int, value: int) -> None:
        # print(f'put({key}, {value})')
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.unlink()
            self.tail.insertLeft(node)
            # print(self.head.toStr())
            return
        
        # ensure capacity
        if len(self.cache) == self.capacity:
            evcit = self.head.next
            evcit.unlink()
            del self.cache[evcit.key]
        
        node = Node(key, value)
        self.cache[key] = node
        self.tail.insertLeft(node)
        # print(self.head.toStr())


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
