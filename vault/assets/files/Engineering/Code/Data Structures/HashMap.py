# Hashing with chaining
# - chain can be a Bucket(array)
# - chain can be a Linked List
class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self, key, value):
        found = False
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = (key, value)
                found = True
        if not found:
            self.bucket.append((key, value))

    def get(self, key):
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket.pop(i)
                break


class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.val = value
        self.next = next

    def update(self, key, value):
        curr, found = self, False
        while curr:
            if curr.key == key:
                curr.val = value
                found = True
                break
            prev = curr
            curr = curr.next
        if not found:
            prev.next = Node(key, value)

    def get(self, key):
        curr = self
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key):
        curr = self
        while curr:
            if curr.key == key:
                prev.next = prev.next.next
                break
            prev = curr
            curr = curr.next


class MyHashMap:
    def __init__(self):
        self.size = 1999
        self.hash_table = [Bucket() for _ in range(self.size)]
        self.hash_table = [Node() for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        i = self.hash(key)
        self.hash_table[i].update(key, value)

    def get(self, key: int) -> int:
        i = self.hash(key)
        return self.hash_table[i].get(key)

    def remove(self, key: int) -> None:
        i = self.hash(key)
        self.hash_table[i].remove(key)
