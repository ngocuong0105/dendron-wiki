# https://leetcode.com/problems/design-hashset/submissions/
class MyHashSet:
    def __init__(self):
        self.size = 10069
        self.hash_table = [None for _ in range(self.size)]

    def hash(self, key, probe):
        return (key % 1999 + probe + probe ** 2) % self.size

    def add(self, key: int) -> None:
        for probe in range(self.size):
            i = self.hash(key, probe)
            if self.hash_table[i] in [key, -1, None]:
                break
        self.hash_table[i] = key

    def remove(self, key: int) -> None:
        for probe in range(self.size):
            i = self.hash(key, probe)
            if self.hash_table[i] in [key, -1, None]:
                self.hash_table[i] = -1
                break

    def contains(self, key: int) -> bool:
        for probe in range(self.size):
            i = self.hash(key, probe)
            if self.hash_table[i] == None:
                return False
            elif self.hash_table[i] == key:
                return True
        return False
