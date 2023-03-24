# Leetcode Daily Challenge

**Date**: March 24th, 2023

**Question**: [1466. Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/)

## Intuition:
*   There are no cycles and only one way to travel between 2 cities.
*   We can construct an undirected graph, keeping track of where the order is reversed.
*   Using this graph, we can traverse from city 0 to every other city and count the number of times we want the "wrong way".

## Solution:
1.  Construct an undirected graph (keeping track of the direction though).
2.  Perform DFS from city 0 counting the number of roads we went the wrong way on.

## Complexity:
### Time: `O(N)` where `N` is the number of cities.
*   **Reasoning**: We perform DFS in the order of `N` time.
### Space: `O(N)` where `N` is the number of cities.
*   **Reasoning**: We keep track of a graph with `N - 1` edges.
