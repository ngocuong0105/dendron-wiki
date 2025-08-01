---
id: 6eu14fdycujs978onqr7jof
title: Memory Management
desc: ''
updated: 1752651662752
created: 1752649655493
---

# Memory Management
```python
del df # does not release memory to the OS
gc.collect() # still does not release memory
```
- Python objects have high-water mark. It is expensive to pull memory from OS so Python interpreter reserves it for future use so in `htop` it looks like memory is being used.
- So in theory when you continue working in the python process you should be able to reclaim this memory with other python objects.
- Yes but unfortunately mostly no... In practice data is fragmented and is not usable unless you close the process (close the interactive terminal)
- Often you will have a *data leak or fragmentation*, meaning the objects are still in memory but not accessible to you. They are scattered around and not usable.

**Hacks**
```python
import os
import psutil

def usage():
    process = psutil.Process(os.getpid())
    return process.memory_info()[0] / float(2**20)


def huge_intermediate_calc(something):
    ...
    huge_df = pd.DataFrame(...)
    ...
    return some_aggregate

import multiprocessing

result = multiprocessing.Pool(1).map(huge_intermediate_calc, [something_])[0]


with multiprocessing.Pool(1) as pool: 
    result = pool.map(huge_intermediate_calc, [something])

# However in a ipython environment (like jupyter notebook) I found that you need to .close() and .join() or .terminate() the pool to get rid of the spawned process.

# Tested example:
def func():
    df = pd.read_parquet(TRAIN_DATA_PATH)
    return df

import concurrent.futures
# max_workers = number of CPUs (threads on your machine, e.g 2 threads per core with8 cores is 16)
print("Number of logical CPUs:", os.cpu_count())
with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
    start_usage = usage()
    print('Start: ', start_usage)
    result = executor.submit(func,).result()
    print('End: ', usage())
    # close process
    executor.shutdown(wait=True)
print(usage())

```

"Then the function is executed at a different process. When that process completes, the OS retakes all the resources it used. Python, pandas, the garbage collector"
- no one can do anything to stop that.

**Some notes and definitions of the aboe tricks**
- Each process is a separate Python interpreter on your local machine (not remote machines).
- ProcessPoolExecutor will not work in the interactive interpreter [docs](https://docs.python.org/3/library/concurrent.futures.html)

# Tracing Python Memory

#TODO

- python library to trace memory allocations [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)


# del and Garbage Collection

"Objects are never explicitly destroyed; however when they become unreachable hey may be garbage-collected."

```python
1 == (1) # returns true
x and (x) usually mean the same thing
del x # this is a statement not a function
del(x) # would do the same thing


(1,) # tuple
```

- `del` deletes the reference, not the object
```python
l1 = [1,2] # l1 reference to the object [1,2]
l2 = l1 # l2 reference to the object
del l1 # deletes reference l1
print(l2) # [1,2]
```

```python
# example of a life of an object
import weakref
def bye():
    print('... goodbye my lover')
ender = weakref.finalize(s1, bye)
ender.alive # True
del s1
ender.alive # True
s2 = '' # ... goodbye my lover
ender.alive # False
```

Objects may be deleted by the garbage collector once they become unreachable! In CPython When the reference count of an object reaches zero, the garbage collector disposes of it. 

# == vs `is`

- `==` compares values, `is` compares if it referencing to the same object

```python
l1 = [1,2]
l2 = l1[::] # make copy
l2 == l1 # true
l1 is l2 # false

l3 = [1,2]

l3 == l2 # true
```


**Garbage Collector**

reference-counting - when it becomes zero it is unreachable and collected.

CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable,
but is not guaranteed to collect garbage containing circular references.


- simple assignment does not create copies - references to the same object
- function parameters are passed as aliases, which means the function may change any mutable object received as an argument. Need to make local copy to prevent this.
- Using mutable objects as default values for function parameters is dangerous because if parameters are changed in-place, the default value is changed!