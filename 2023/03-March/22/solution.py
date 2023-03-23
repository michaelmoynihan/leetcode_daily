from collections import defaultdict
from typing import Sequence, Tuple


class Solution:
    def minScore(self, n: int, roads: Sequence[Tuple[int, int, int]]) -> int:
        # Construct the undirected graph.
        graph = defaultdict(list)
        for a, b, w in roads:
            graph[a].append((b, w))
            graph[b].append((a, w))

        # Keep track of the visited edges and the minimum weight. Perform DFS.
        visited = set()
        min_weight = float('inf')
        stack = [1]
        while stack:
            node = stack.pop()
            for neighbor, w in graph[node]:
                # If the edge from node to neighbor has been traversed, don't
                # traverse again.
                if (node, neighbor) in visited or (neighbor, node) in visited:
                    continue

                # Update the minimum weight, set the edge as visited and add
                # the neighbor to the stack.
                min_weight = min(min_weight, w)
                visited.add((node, neighbor))
                stack.append(neighbor)
        return min_weight
