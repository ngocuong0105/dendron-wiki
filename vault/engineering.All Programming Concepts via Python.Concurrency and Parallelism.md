---
id: 0364m0da0huw23ds7lo5wqk
title: Concurrency and Parallelism
desc: ''
updated: 1752649728068
created: 1752649320880
---


# Concurrency Models in Python

Chapter 19 from "Fluent Python"

Concurrency is about dealing with multiple things at once.

Parallelism is about doing multiple things at once.

Concurrency is about structure, Parallelism is about execution.

A CPU with 4 cores can run 4 processes in parallel but 100s processes concurrently. 



# Old notes

- concurrent, multithreaded programming, [web crawler](https://leetcode.com/problems/web-crawler-multithreaded/)
```Python
# simple DFS
class Solution:
    def crawl(self, start: str, parser: 'HtmlParser') -> List[str]:
        hostname = lambda x: x.split('/')[2]
        visited,stack= set([start]),[start]
        while stack:
            s = stack.pop()
            for u in parser.getUrls(s):
                if u not in visited and hostname(start) == hostname(u):
                    visited.add(u)
                    stack.append(u)
        return visited

# concurrent DFS
from concurrent import futures
class Solution:
    def crawl(self, s: str, parser: 'HtmlParser') -> List[str]:
        hostname = lambda x: x.split('/')[2]
        visited = set([s])
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = [executor.submit(parser.getUrls, s)]
            while tasks:
                neigh = tasks.pop().result()
                for u in neigh:
                    if u not in visited and hostname(s) == hostname(u):
                        visited.add(u)
                        tasks.append(executor.submit(parser.getUrls, u))
        return visited
```

# Deadlocks and how to properly acquire release locks

```python
from threading import Lock
```

Common examples of the cause of threading deadlocks include:

- A thread that waits on itself (acquires itself twice releases once and waits for itself)
- Threads that wait on each other (e.g. A waits on B, B waits on A).
- Thread that fails to release a resource (e.g. mutex lock, semaphore, barrier, condition, event, etc.).
- Threads that acquire mutex locks in different orders (e.g. fail to perform lock ordering).


```python
from threading import Lock
lock = Lock()
lock.acquire()
lock.acquire()
lock.release() # deadlock

# no deadlock I think
lock.acquire()
lock.release() 
lock.acquire()

```
- [Print Order](https://leetcode.com/problems/print-in-order/)

- [FizzBuzz](https://leetcode.com/problems/fizz-buzz-multithreaded/)

malko e mazalo...

```python
from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.finish = False
        self.fizz_lock = Lock()
        self.buzz_lock = Lock()
        self.fizzbuzz_lock = Lock()
        self.main = Lock()
        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizz_lock.acquire()
            if self.finish: return
            printFizz()
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzz_lock.acquire()
            if self.finish: return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzz_lock.acquire()
            if self.finish: return
            printFizzBuzz()
            self.main.release()
            
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1):
            self.main.acquire()
            if i % 3 == 0 and i % 5 != 0: self.fizz_lock.release()
            elif i % 3 != 0 and i % 5 == 0: self.buzz_lock.release()
            elif i % 3 == 0 and i % 5 == 0: self.fizzbuzz_lock.release()
            else:
                printNumber(i)
                self.main.release()
        
        self.main.acquire()
        self.finish = True
        self.buzz_lock.release()
        self.fizz_lock.release()
        self.fizzbuzz_lock.release()


```


GOAL: Run only one thread at a time!!!!!

Racing conditions are dangerous.