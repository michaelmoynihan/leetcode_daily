from collections import defaultdict
from typing import Mapping, Sequence


class Solution:
    def numConnectedComponents(self, n: int,
                               graph: Mapping[int, Sequence[int]]) -> int:
        # Keep track of which nodes we have already visited and how many
        # components we have see.
        visited = [False] * n
        num_components = 0
        for node in range(n):
            if visited[node]:
                continue

            # Add another component if we have not already seen this node.
            num_components += 1

            # Use DFS to visit all nodes connected to this node.
            stack = [node]
            while stack:
                top = stack.pop()
                if visited[top]:
                    continue
                visited[top] = True
                for neighbor in graph[top]:
                    if visited[neighbor]:
                        continue
                    stack.append(neighbor)
        return num_components

    def makeConnected(self, n: int, connections: Sequence[Sequence[int]]) -> int:
        # Edge case: The problem cannot be solved if there are fewer than `n-1`
        # edges.
        if len(connections) < n - 1:
            return -1

        # Construct the graph.
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        # Return the number of connected components - 1.
        return self.numConnectedComponents(n, graph) - 1
