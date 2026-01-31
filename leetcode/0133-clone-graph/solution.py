"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_node = Node(node.val)
        self.visited[node] = new_node

        new_neighbors = []
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                new_neighbors.append(self.visited[neighbor])
            else:
                new_neighbors.append(self.cloneGraph(neighbor))
        new_node.neighbors = new_neighbors
        return new_node
        
