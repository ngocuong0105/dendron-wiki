#%%
from collections import defaultdict
from distutils.command.build import build
from typing import List
class SegmentTree:
    def __init__(self, update_fn, query_fn):
        '''
        for summation tree: query_fn = update_fn = lambda x,y: x+y 
        works if these two with the space of the values form a semiring
        '''
        self.UF, self.QF = update_fn, query_fn
        self.T = defaultdict(int) # [0]*4*n

    def update(self, v, tl, tr, pos, delta):
        '''
        v is the index of the node (we use 1-indexing, as v has children 2v, 2(v+1))
        (v,tl,tr) is root node, e.g. (1,0,n-1)
        The tree nodes are represented using the index v and INCLUSIVE intervals [tl,tr]
        Updates SINGLE value at position pos by coposing delta with UF (e.g. adding delta)
        '''
        if tl == tr: 
            self.T[v] = self.UF(self.T[v], delta)
        else:
            tm = (tl + tr)//2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, delta)
            else:
                self.update(v*2+1, tm+1, tr, pos, delta)
            self.T[v] = self.QF(self.T[v*2], self.T[v*2+1])

    def query(self, v, tl, tr, l, r):
        '''
        (v,tl,tr) is root node, e.g. (1,0,n-1)
        returns QF[l:r+1], e.g. sum(nums[l:l+r]) if QF = lambda x,y: x+y 
        '''        
        if l > r: return 0
        if l == tl and r == tr: return self.T[v]
        tm = (tl + tr)//2
        return self.QF(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))

st = SegmentTree(lambda x,y:x+y, lambda x,y: x+y)
# %%
class SegmentTree:
    def __init__(self, update_fn, query_fn):
        self.UF, self.QF = update_fn, query_fn
        self.T = defaultdict(int)   # [0] * (4*N)
        self.L = defaultdict(int)   # [0] * (4*N), keep info for whole segment when making range updates
 
    # lazy propagation
    def push(self, v):
        for u in [2*v, 2*v+1]:
            self.T[u] = self.UF(self.T[u], self.L[v])
            self.L[u] = self.UF(self.L[u], self.L[v])
        self.L[v] = 0

    def update(self, v, tl, tr, l, r, h):
        if l > r: return
        if l == tl and r == tr:
            self.T[v] = self.UF(self.T[v], h)
            self.L[v] = self.UF(self.L[v], h)
        else:
            self.push(v)
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)
            self.T[v] = self.QF(self.T[v*2], self.T[v*2+1])

    def query(self, v, tl, tr, l, r):
        if l > r: return -float("inf")
        if l == tl and tr == r: return self.T[v]
        self.push(v)
        tm = (tl + tr)//2
        return self.QF(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))
# %%
