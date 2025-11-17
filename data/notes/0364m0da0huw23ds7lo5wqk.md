

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


# Native Coroutines


Python has three ways to run things concurrently
- coroutines (classic and native)
- threads
- processes

Native coroutines use asyncio library using `async def` and `await` syntax
- `asyncio` is a library that allows the USER to manually create an event loop (with ONE THREAD) and schedule tasks to run concurrently
- Allows YOU to multitask with functions!
- asyncio is Python’s **standard library**
- **Run time of concurrently ran functions = Run time of slowest function**, if you schedule the tasks to run in the background!

## Creating Background Task

say you have two functions one that takes 10 seconds and one that takes 5 seconds, how can you run them concurrently?
```python
import asyncio

async def slow():
    print("Starting slow")
    await asyncio.sleep(10)
    print("Ended slow")

async def calc_that_does_not_wait_slow():
    await asyncio.sleep(5)
    print(1)


async def main():
      await calc_that_does_not_wait_slow()
      await slow()
import time
print(start:= time.time())
await main()
print(end:= time.time())
print(end-start)

# takes 15 seconds
# even if you swap 
#       await calc_that_does_not_wait_slow()
#       await slow()
# it will take 15 seconds
```

**You need to make them one as background task!** Currently you are running code sequentially.


```python
import asyncio
async def slow():
    print('starting slow')
    await asyncio.sleep(10)
    print('ended slow')

async def calc_that_does_not_wait_slow():
    await asyncio.sleep(5)
    print(1)

async def main():
    slow_task = asyncio.create_task(slow()) 
    await calc_that_does_not_wait_slow()
# Outside main:
print(start:= time.time())
await main()
print(end:= time.time())
print(end-start)
# Prints 5 seconds only! And 5 seconds after prints ended slow!
#  How it runs: 
#
#      slow() is started in the background (will take 10 seconds).
#      You immediately start and await calc_that_does_not_wait_slow() (waits 5 seconds, then prints 1).
#      When calc_that_does_not_wait_slow() is done (after 5 seconds), main() returns—even if slow() is still running!
#      The program ends; slow() may be cancelled or left unfinished.
     
```

**Lets await the task and the calculation now.**
- await the slow first and then the other -> 15 seconds - sad
```python
import asyncio

async def slow():
    print("Starting slow")
    await asyncio.sleep(10)
    print("Ended slow")

async def calc_that_does_not_wait_slow():
    await asyncio.sleep(5)
    print(1)


async def main():
      slow_task = asyncio.create_task(slow()) # background task
      await slow_task
      await calc_that_does_not_wait_slow()
import time
print(start:= time.time())
await main()
print(end:= time.time())
print(end-start)

# Output
# 1754464873.7352946
# Starting slow
# Ended slow
# 1
# 1754464888.7525644
# 15.017269849777222
```

- await the  slow after and it takes 10 seconds
```python
import asyncio

async def slow():
    print("Starting slow")
    await asyncio.sleep(10)
    print("Ended slow")

async def calc_that_does_not_wait_slow():
    await asyncio.sleep(5)
    print(1)


async def main():
      slow_task = asyncio.create_task(slow())
      await calc_that_does_not_wait_slow()
      await slow_task
import time
print(start:= time.time())
await main()
print(end:= time.time())
print(end-start)

# Output 
# 1754464849.4491456
# Starting slow
# 1
# Ended slow
# 1754464859.4551563
# 10.00601077079773
```

## Background tasks are confusing - just use gather!

```python
import asyncio

async def slow():
    print("Starting slow")
    await asyncio.sleep(10)
    print("Ended slow")

async def calc_that_does_not_wait_slow():
    print(1)

async def main():
    # Both coroutines start at once; don't wait for one to finish before the other
    await asyncio.gather(slow(), calc_that_does_not_wait_slow())

# will run for 10 seconds as well
```

### Summary

 

**Concurrent async functions:**

- If you want two async functions (coroutines) to run simultaneously, you must schedule them to run at the same time.
- await-ing one after the other causes them to run sequentially, so the total run time is the sum of both delays.
     


**Background tasks with create_task:**

- Using asyncio.create_task(coro()) starts a coroutine in the background.
- If you don't later await the task, your program may exit before the background task finishes.
- If you start the slow task in the background and only await the fast task, the program finishes after the fast task—even if the slow one hadn't finished yet (the slow one is cancelled or left unfinished).


