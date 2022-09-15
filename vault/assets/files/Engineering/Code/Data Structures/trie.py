# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://leetcode.com/problems/prefix-and-suffix-search/
# Dictionary implementation
# Would not support predecessor/successor
# Need to do array if want these
# More complicated implementations with BST, weighted Balanced Trie in Advanced data structures.
# See Advanced Data structures course in MIT
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        # map from characters to nodes
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts the string word into the trie.
        """
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word) -> bool:
        """
        Returns true if the string word is in the trie
        (i.e., was inserted before), and false otherwise.
        """
        curr = self.root
        for char in word:
            curr = curr.children.get(char)
            if curr == None:
                return False
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string
        word that has the prefix prefix, and false otherwise.

        """
        curr = self.root
        for char in prefix:
            curr = curr.children.get(char)
            if curr == None:
                return False
        return True

#%%
from collections import defaultdict

# Alternatively drop TriNode -> self is your node

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True