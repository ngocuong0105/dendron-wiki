import string
import collections


class Solution:
    """
    Hashing Solution. Faster than sorting each word. However, could avoid hash
    if we just copare the count of distict characters in each word (this is
    what we care in anagrams).
    """

    def __init__(self):
        # O(1)
        self.d = dict(zip(string.ascii_lowercase, self.get_primes(26)))

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = collections.defaultdict(list)
        # O(len(strs)*len(word))
        for word in strs:
            count = collections.Counter(word)
            d[self.h(count)].append(word)
        return [val for _, val in d.items()]

    def get_primes(self, n):
        res = [2]
        while len(res) < n:
            p = res[-1] + 1
            while not self.isPrime(p):
                p += 1
            res.append(p)
        return res

    def isPrime(self, p):
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                return False
        return True

    def h(self, count: "collections.Counter") -> int:
        res = 1
        for key, val in count.items():
            res *= self.d[key] ** val
        return res
