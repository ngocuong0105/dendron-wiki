class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head,self.tail = Node(),Node()
        self._link(self.head,self.tail)
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key].val
        self._move_front(self.cache[key])
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
        node = Node(key,value)    
        self._add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            last = self.tail.prev
            self._delete(last)
            del self.cache[last.key]

    def _link(self, n1, n2):
        n1.next, n2.prev = n2, n1

    def _add(self, node):
        self._link(node, self.head.next)
        self._link(self.head, node)

    def _delete(self, node):
        self._link(node.prev, node.next)

    def _move_front(self, node):
        self._delete(node)
        self._add(node)
