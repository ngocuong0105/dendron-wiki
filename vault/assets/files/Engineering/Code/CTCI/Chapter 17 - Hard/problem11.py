# https://leetcode.com/problems/shortest-word-distance-ii/submissions/
import collections


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.d = collections.defaultdict(list)
        for i in range(len(wordsDict)):
            self.d[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        l1, l2 = self.d[word1], self.d[word2]
        res = abs(l1[i] - l2[j])
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return res
