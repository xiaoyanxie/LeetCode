from collections import defaultdict

class Node:
    def __init__(self, freq=None, keys={}):
        self.freq = freq
        self.keys = keys
        self.next = None
        self.prev = None

    def unlink(self):
        self.prev.next, self.next.prev = self.next, self.prev
        self.prev, self.next = None, None

    def anyKey(self):
        return next(iter(self.keys))

    def insertLeft(self, node):
        self.prev.next = node
        node.prev = self.prev

        self.prev = node
        node.next = self
        
    def insertRight(self, node):
        self.next.prev = node
        node.next = self.next

        self.next = node
        node.prev = self

class AllOne:

    def __init__(self):
        # key -> #freq
        self.freq = defaultdict(int)
        # #freq -> Node(#freq, {k1, k2, k3, ...})
        self.freqgrp = {}
        self.head = Node(freq=-inf)
        self.tail = Node(freq=inf)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeOldFreqRecord(self, key):
        if key not in self.freq:
            return None, None
        
        assert self.freq[key] in self.freqgrp
        node = self.freqgrp[self.freq[key]]
        node.keys.remove(key)
        prev, nxt = node.prev, node.next
        if not node.keys:
            node.unlink()
            del self.freqgrp[self.freq[key]]
        return prev, nxt

    def updateNewFreqRecord(self, key, target):
        assert key in self.freq
        if self.freq[key] in self.freqgrp:
            self.freqgrp[self.freq[key]].keys.add(key)
            return
        
        node = Node(freq=self.freq[key], keys={key})
        self.freqgrp[self.freq[key]] = node
        
        if not target:
            self.head.insertRight(node)
        elif node.freq < target.freq:
            target.insertLeft(node)
        else:
            target.insertRight(node)

    def inc(self, key: str) -> None:
        _, nxt = self.removeOldFreqRecord(key)
        self.freq[key] += 1
        self.updateNewFreqRecord(key, nxt)

    def dec(self, key: str) -> None:
        prev, _ = self.removeOldFreqRecord(key)
        self.freq[key] -= 1
        if self.freq[key] == 0:
            del self.freq[key]
            return
        self.updateNewFreqRecord(key, prev)

    def getMaxKey(self) -> str:
        return self.tail.prev.anyKey() if self.freqgrp else ''

    def getMinKey(self) -> str:
        return self.head.next.anyKey() if self.freqgrp else ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
