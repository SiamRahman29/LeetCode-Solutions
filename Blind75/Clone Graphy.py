class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    memo = {}
    def cloneNode(node):
        if not node:
            return None
        if node in memo:
            return memo[node]
        copy = Node(node.val)
        memo[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(cloneNode(nei))
        return copy
    return cloneNode(node)
