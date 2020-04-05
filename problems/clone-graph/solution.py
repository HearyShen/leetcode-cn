"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        visited = {}

        def dfs(node):
            if not node:
                return
            if node.val in visited:
                return visited[node.val]
            cloneNode = Node(node.val, [])
            visited[cloneNode.val] = cloneNode
            if node.neighbors:
                for neighbor in node.neighbors:
                    cloneNode.neighbors.append(dfs(neighbor))
            return cloneNode

        return dfs(node)