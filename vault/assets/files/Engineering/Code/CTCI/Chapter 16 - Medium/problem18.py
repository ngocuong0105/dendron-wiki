# https://leetcode.com/problems/word-pattern/
import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        pattern = list(pattern)
        if len(pattern) != len(words):
            return False
        d = collections.defaultdict(set)
        for i in range(len(words)):
            d[words[i]].add(pattern[i])
            if len(d[words[i]]) > 1:
                return False
        d = collections.defaultdict(set)
        for i in range(len(words)):
            d[pattern[i]].add(words[i])
            if len(d[pattern[i]]) > 1:
                return False
        return True
