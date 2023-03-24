# Leetcode Daily Challenge

**Date**: March 19th, 2023

**Question**: [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

## Intuition:
*   A Trie (prefix tree) is the perfect data structure to store words with minimal space and quick look up.
*   In Python, stack frames are expensive, so we will just make each node a dictionary.
    *   E.g. If we add "bad", we will get `{'b':{'a':{'d':{}}}}`. Then say we added "bam" as well, we would get `{'b':{'a':{'d':{}, 'm': {}}}}`
*   With Tries, we need some notion of where a word ends (e.g. If we have `cat` and `cats`). One way we can solve this is by keeping a boolean at each node, but I suspect we will get a substantial speed up by keeping a different root for each length of word. Therefore, we will have a separate Trie for each length to avoid this problem.

## Solution:
1.  Add word: iterate over our existing Trie for the length of the word and our word adding nodes to the Trie as necessary.
2.  Search word: use recursion. If we have a `.`, then we recurse on each present letter.

## Complexity:
### Add Word
#### Time: `O(N)` where `N` is the length of the word.
*   **Reasoning**: We iterate over the array one time.
#### Space: `O(N)` where `N` is the length of the word.
*   **Reasoning**: At worst, we add a node for each visited letter.
### Search Word:
#### Time and Space Complexities are not easy to determine.
