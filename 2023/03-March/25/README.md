# Leetcode Daily Challenge

**Date**: March 25th, 2023

**Question**: [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/)

## Intuition:
*   We really care about connected components here.
*   If I have n nodes and a component has 5 nodes, then I know that the number of pairs between the two are (n - 5) * 5.
*   I can repeat this logic for all components, but need to make sure not do double count.

## Solution:
1.  Construct an undirected graph (keeping track of the direction though).
2.  Find the connected components. For each connected component, if it has size k, add `k * (remaining - k)` to the result, where `remaining` is the number of unvisited nodes (this way we prevent double counting).

## Complexity:
### Time: `O(N)` where `N` is the number of nodes.
*   **Reasoning**: We perform DFS in the order of `N` time.
### Space: `O(N + E)` where `N` is the number of nodes and `E` is the number of edges.
*   **Reasoning**: We keep track of a graph with `N` nodes and `E` edges.
