from collections import defaultdict
import string
from typing import Any, Mapping


class WordDictionary:
    def __init__(self):
        self.trie_by_len = defaultdict(dict)

    def addWord(self, word: str) -> None:
        d = self.trie_by_len[len(word)]
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

    def search(self, word: str) -> bool:
        def helper(word: str, i: int, d: Mapping[int, Any]) -> bool:
            if i == len(word):
                return True
            if word[i] == '.':
                for c in string.ascii_lowercase:
                    if c in d and helper(word, i + 1, d[c]):
                        return True
                return False
            if word[i] not in d:
                return False
            return helper(word, i + 1, d[word[i]])
        return helper(word, 0, self.trie_by_len[len(word)])
