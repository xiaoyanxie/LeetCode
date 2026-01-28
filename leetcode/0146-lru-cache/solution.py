class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.mp = {}

    def __remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def __add_to_tail(self, node):
        t, tp = self.tail, self.tail.prev
        tp.next = node
        node.prev = tp
        t.prev = node
        node.next = t

    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]
            self.__remove(node)
            self.__add_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.__remove(node)
            self.__add_to_tail(node)
            return

        if len(self.mp) == self.capacity:
            rm = self.head.next
            self.__remove(rm)
            del self.mp[rm.key]
        
        node = Node(key, value)
        self.mp[key] = node
        self.__add_to_tail(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
