# Leetcode Daily Challenge

**Date**: March 21rd, 2023

**Question**: [2348. Number of Zero-Filled Subarrays
](https://leetcode.com/problems/number-of-zero-filled-subarrays/description/)

## Intuition:
*   Given an array of 0's of length `N`, we can form `N` arrays of length `1`, `N - 1` arrays of length `2`, ..., `1` array of length `N`.
*   `1 + 2 + ... + N = (N * (N + 1)) / 2`.

## Solution:
1.  Find each largest subarray of 0's.
2.  Use our equation to count the number of subarrays contained in that subarray.

## Edge Cases:
*   The problem cannot be solved if there are fewer than `n-1` edges.

## Complexity:
### Time: `O(N)` where `N` is the length of the array.
*   **Reasoning**: We iterate over the array one time.
### Space: `O(1)`.
*   **Reasoning**: We only store the result in an integer.
