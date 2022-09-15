'''
Iterators = Streams of data

Iterator properties:

The first property of an Iterator that we'll looked at is that it only needs to know how to get the next item.
(see LinkedListIterator)

It doesn't need to store the entire data in memory if we don't need the entire data structure.
Notice we store the head at the start, but as items are consumed, we discard the current one and replace it with
the item in the node after


The second property of Iterators is that they can represent sequences without even using a data structure!
(see RangeIterator) This shows that range(1,100000) is O(1) space!

The third property is that iterators handle infinite sequences

Side note: check range_custom() in the end for functional approach.
'''
class Node:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class LinkedListIterator:

    def __init__(self):
        self.head = Node()

    def next(self):
        val = self.head.val
        self.head = self.head.next
        return val

    def has_next(self):
        return self.head.val is not None


class RangeIterator:

    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def next(self):
        val = self.start
        self.start += self.step
        return val

    def has_next(self):
        return self.start < self.end


class SquaresIterator:
    def __init__(self):
        self._n = 0

    def next(self):
        result = self._n
        self._current += 1
        return result ** 2

    def has_next(self):
        return True

def range_custom(start, end):
    while start < end:
        yield start
        start += 1
