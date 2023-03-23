# Leetcode Daily Challenge

**Date**: March 22rd, 2023

**Question**: [2492. Minimum Score of a Path Between Two Cities
](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/)

## Intuition:
*   Doing DFS from node `1` to node `n` does not cover all edges that we could visit.
*   If we store visited edges instead of visited nodes, we can make sure we don't visit the same edge multiple times when doing DFS.

## Solution:
1.  Construct a graph.
2.  Perform DFS, storing the visited edges instead of the visited nodes.

## Complexity:
### Time: `O(E)` where `E` is the number of roads.
*   **Reasoning**: Constructing the graph requires `O(E)` time, because we have to iterate over each edge. Performing DFS requires `O(E)` time, because we visit each visitable edge.
### Space: `O(min(N, E))` where `N` is the number of cities and `E` is the number of roads.
*   **Reasoning**: Constructing the graph requires `O(E)` space, because for each edge we store a constant amount of information in our graph. Performing DFS requires `O(E)` memory in the worst case.
