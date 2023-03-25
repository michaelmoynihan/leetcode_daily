from collections import defaultdict
from typing import Sequence


class Solution:
    def countPairs(self, n: int, edges: Sequence[Sequence[int]]) -> int:
        # Construct an undirected graph.
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Find the connected components. For each connected component, multiply its
        # size by the remaining unvisited elements.
        result, remaining = 0, n
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            size = 0
            stack = [i]
            while stack:
                top = stack.pop()
                if visited[top]:
                    continue
                visited[top] = True
                size += 1
                remaining -= 1
                for neighbor in graph[top]:
                    if visited[neighbor]:
                        continue
                    stack.append(neighbor)
            result += size * remaining
        return result
