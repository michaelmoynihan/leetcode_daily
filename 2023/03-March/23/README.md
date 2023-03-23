# Leetcode Daily Challenge

**Date**: March 23rd, 2023

**Question**: [1319. Number of Operations to Make Network Connected
](https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/)

## Intuition:
*   If all of the computers are connected, 0 edges need to be moved.
*   If there are 2 connected components, 1 edge needs to be moved.
*   If there are n components, `n-1` edges need to be moved.

## Solution:
1.  Construct a graph.
2.  Find the number of connected components by doing DFS starting at each unvisited node.

## Edge Cases:
*   The problem cannot be solved if there are fewer than `n-1` edges.

## Complexity:
### Time: `O(min(N, E))` where `N` is the number of computers and `E` is the number of edges.
*   **Reasoning**: Constructing the graph requires `O(E)` time, because we have to iterate over each edge. Performing DFS requires `O(N)` time, because we visit each node.
### Space: `O(min(N, E))` where `N` is the number of computers and `E` is the number of edges.
*   **Reasoning**: Constructing the graph requires `O(E)` space, because for each edge we store a constant amount of information in our graph. Performing DFS requires `O(N)` memory in the worst case.
