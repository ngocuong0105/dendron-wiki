# Design a leader board = key value store sorted by values = ordered dictionary
# https://leetcode.com/problems/design-a-leaderboard/solution/

from heapq import heappop, heappush


# simple array
class Leaderboard:

    def __init__(self):
        self.scores = []

    # O(n)
    def addScore(self, playerId: int, score: int) -> None:
        for i in range(len(self.scores)):
            if self.scores[i][1] == playerId: 
                self.scores[i][0] += score
                return 
        self.scores.append([score,playerId])
        
    # O(nlogn)
    def top(self, K: int) -> int:
        self.scores.sort(reverse = True)
        return sum(s for s,_ in self.scores[:K])

    # O(n)
    def reset(self, playerId: int) -> None:
        for i in range(len(self.scores)):
            if self.scores[i][1] == playerId: break
        self.scores.pop(i)
        
# simple hashmap
class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        
    # O(1)
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        
    # O(nlogn)
    def top(self, K: int) -> int:
        vals = sorted(self.scores.values())[-K:]
        return sum(s for s in vals)

    # O(1)
    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        
# HashMap + heap inside top
class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
    
    # O(1)
    def addScore(self, p: int, score: int) -> None:
        self.scores[p] -= score
        
    # O(n*logk)
    def top(self, k: int) -> int:
        res = 0
        h = []
        for v in self.scores.values():
            heappush(h,-v)
            if len(h) > k: heappop(h)
        return sum(h)
        
    # O(1)
    def reset(self, p: int) -> None:
        del self.scores[p]

# HashMap + heap lazy delete/introduce delay delay, priority queue/ message queu
class Leaderboard:

    def __init__(self):
        self.heap = []
        self.scores = defaultdict(int)
    
    # O(logn)
    def addScore(self, p: int, score: int) -> None:
        self.scores[p] -= score
        heappush(self.heap,(self.scores[p],p))
    
    # (k*logn)
    def top(self, k: int) -> int:
        res,cnt = 0,0
        backup = []
        while k:
            score,p = heappop(self.heap)
            if self.scores.get(p,0) == score:
                backup.append((score,p))
                res -= score
                k -= 1
        for t in backup:
            heappush(self.heap,t)
        return res
    
    # O(1)
    def reset(self, p: int) -> None:
        del self.scores[p]
    
# Double link list
class Node(object):
    def __init__(self, score):
        self.score = score
        self.prev = None
        self.next = None

class Leaderboard(object):

    def __init__(self):
        self.players = {}
        self.header = Node(float('inf'))
        self.tailer = Node(-float('inf'))
        self.header.next = self.tailer
        self.tailer.prev = self.header

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # O(n)
    def _insert(self, node):
        p = self.header
        while p.score > node.score:
            p = p.next
        p.prev.next = node
        node.prev = p.prev
        p.prev = node
        node.next = p
    
    # O(n)
    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId in self.players:
            node = self.players[playerId]
            node.score += score
            self._remove(node)
        else:
            node = Node(score)
            self.players[playerId] = node
        self._insert(node)

    # O(k)
    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        rtn = 0
        k = 0
        p = self.header.next
        while k<K and p != self.tailer:
            rtn += p.score
            p = p.next
            k+=1
        return rtn
    
    # O(1)
    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        node = self.players[playerId]
        self._remove(node)
        del self.players[playerId]

# SortedDict
from collections import defaultdict
from sortedcontainers import SortedDict
        
class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int) # playerId: score
        self.sortedScores = SortedDict()  # score: number of players with that score  
    
    # O(log N)
    def addScore(self, playerId: int, score: int) -> None:
        preScore = self.scores[playerId]
        if preScore:
            self.sortedScores[preScore] -= 1
            if self.sortedScores[preScore] == 0: del self.sortedScores[preScore]
        
        score = - score
        self.scores[playerId] += score
        key = self.scores[playerId]
        self.sortedScores.update({key:self.sortedScores.get(key,0)+1})
        
    # O(K)
    def top(self, K: int) -> int:
        # print(self.sortedScores)
        res = 0
        for score,cnt in self.sortedScores.items():
            res -= score*min(K,cnt)
            K -= min(K,cnt)
            if K == 0: return res
        
    # O(log N)
    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        del self.scores[playerId]
        self.sortedScores[score] -= 1
        if self.sortedScores[score] == 0: del self.sortedScores[score]
            
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)