# Leetcode Daily Challenge

**Date**: March 20rd, 2023

**Question**: [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/)

## Intuition:
*   Try to place flowers at each available plot using a greedy approach.

## Solution:
1.  Iterate over the array. If the current plot and the plots on either side are unoccupied, plant a flower.
2.  If we planted enough flowers, return True; otherwise, return False.

## Edge Cases:
*   If it is the first plot, we don't need to check before the plot.
*   If it is the last plot, we don't need to check after the plot.

## Complexity:
### Time: `O(N)` where `N` is the length of the array.
*   **Reasoning**: We iterate over the array one time.
### Space: `O(1)`.
*   **Reasoning**: We update the input array in place.
