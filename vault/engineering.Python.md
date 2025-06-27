---
id: 7khpigcji0ufpuptuqozcft
title: Python
desc: ''
updated: 1751026341893
created: 1750781063837
---

- [Python Language Reference](https://docs.python.org/3/reference/datamodel.html)
- [Fluent Python Book](https://elmoukrie.com/wp-content/uploads/2022/05/luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.pdf)


# Memory Management
```python
del df # does not release memory to the OS
gc.collect() # still does not release memory
```
- Python objects have high-water mark. It is expensive to pull memory from OS so Python interpreter reserves it for future use so in `htop` it looks like memory is being used.
- So in theory when you continue working in the python process you should be able to reclaim this memory with other python objects.
- Yes but unfortunately mostly no... In practice data is fragmented and is not usable unless you close the process (close the interactive terminal)
- Often you will have a *leak or fragmentation*

**Hacks**
```python
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

with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
    start_usage = usage()
    print('Start: ', start_usage)
    result = executor.submit(func,).result()
    print('End: ', usage())
    # close process
    executor.shutdown(wait=True)
print(usage())

```

Then the function is executed at a different process. When that process completes, the OS retakes all the resources it used. Python, pandas, the garbage collector
- no one can do anything to stop that.

# Tracing Python Memory

#TODO

- python library to trace memory allocations [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)



# Private methods
Private methods are those methods which can't be accessed in other class except the class in which they are declared.

- One underscore is to show it is a internal function: `_function_name()`
- Two underscores: the idea is to use double __ to fully disclose methods as private so python will convert them form __private_method to _Myclass__my_private_method and will not let a child class overwrite this method. 

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

# Python Data Model

- [Data Model from Python Language Reference](https://docs.python.org/3/reference/datamodel.html)


Every object has identity (address of the place in memory), type and value. Only value can be changed (for mutable objects). Immutable objects cannot have their value changed.

`is` operator compares the identity of two objects `==` compares their value.

`id()` gives an integer representing the identity


# Concurrency Models in Python

Chapter 19 from "Fluent Python"

Concurrency is about dealing with multiple things at once.

Parallelism is about doing multiple things at once.

Concurrency is about structure, Parallelism is about execution.

A CPU with 4 cores can run 4 processes in parallel but 100s processes concurrently. 




# Polars lazy API

Write query plan first and run only when needed, i.e. collect()


the lazy API:
- has query optimizations like in (SQL). You tell it what to do not how to do it so it arranges the queries is the most optimal way
- allows to work with larger than memory datasets using streaming
- [list of optimizations](https://docs.pola.rs/user-guide/lazy/optimizations/) - all is related to optimal query planning
- schema plays important role. The lazy API does type checking before running all expensive queries!
- This Polars query optimizer MUST be able to infer the schema at every step of the query plan (hence .pivot() operation is not available - creates columns from values coming in one column). The optimizer does not know in advance these column names
- visualize optimizations using `.show_graph()` read from bottom to top. sigma is (filtering rows), pi is projection (filtering columns) -> here you will see how polars does predicate pushdown and projection pushdown
- Remember that LazyFrames are query plans i.e. a promise on computation and is not guaranteed to cache common subplans.
- sinks - saving data to disk without the need to load the whole dataset in memory. Process data in batches/chunks. I.e. we are streaming the results to storage

**Tricks**

`pl.scan_csv` or `pl.scan_parquet`

- read files larger than memory
```python
# With the default collect method Polars processes all of your data as one batch. This means that all the data has to fit into your available memory at the point of peak memory usage in your query.
# So do: 
.collect(engine='streaming') # to read datasets thar are larger than memory
```

- Sink
```python
# sink = streaming data to storage - saving in batches
lf = scan_csv("my_dataset/*.csv").filter(pl.all().is_not_null())
lf.sink_parquet(
    pl.PartitionMaxSize(
        "my_table_{part}.parquet"
        max_size=512_000
    )
)

# creates
# my_table_0.parquet
# my_table_1.parquet
# ...
# my_table_n.parquet
```

- diverging queries (kind of caching..)
- [Multiplexing queries](https://docs.pola.rs/user-guide/lazy/multiplexing/)! (also group_by does not guarantee order)
```python
# Some expensive LazyFrame
lf: LazyFrame

lf_1 = LazyFrame.select(pl.all().sum())

lf_2 = lf.some_other_computation()

pl.collect_all([lf_1, lf_2]) # this will execute lf only once!
```
