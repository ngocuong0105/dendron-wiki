# https://leetcode.com/problems/implement-trie-ii-prefix-tree/submissions/
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_cnt = 0
        self.rank = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            curr.rank += 1
        curr.word_cnt += 1

    def countWordsEqualTo(self, word: str) -> int:
        """
        Returns the number of instances of the string word in the trie.
        """
        curr = self.root
        for char in word:
            curr = curr.children.get(char)
            if curr == None:
                return 0
        return curr.word_cnt

    def countWordsStartingWith(self, prefix: str) -> int:
        """
        Returns the number of strings in the trie that have the string prefix as a prefix.
        """
        curr = self.root
        for char in prefix:
            curr = curr.children.get(char)
            if curr == None:
                return 0
        return curr.rank

    def erase(self, word: str) -> None:
        """
        Erases the string word from the trie.
        Assumed that for any function call to erase, the string word will exist in the trie.
        """
        if self.countWordsEqualTo(word) > 0:
            curr = self.root
            for char in word:
                curr = curr.children.get(char)
                curr.rank -= 1
            curr.word_cnt -= 1
