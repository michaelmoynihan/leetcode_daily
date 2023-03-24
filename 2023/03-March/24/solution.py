from collections import defaultdict
from typing import Sequence


class Solution:
    def minReorder(self, n: int, connections: Sequence[Sequence[int]]) -> int:
        # Create an undirected graph where `True` represents the correct direction and
        # `False` represents the wrong direction.
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, False))
            graph[b].append((a, True))

        # Perform DFS and count the number of edges that must be reversed.
        count = 0
        visited = [False] * n
        stack = [(0, True)]
        while stack:
            top, correct_direction = stack.pop()
            if not correct_direction:
                count += 1
            if visited[top]:
                continue
            visited[top] = True
            for neighbor, correct_direction in graph[top]:
                if visited[neighbor]:
                    continue
                stack.append((neighbor, correct_direction))
        return count
