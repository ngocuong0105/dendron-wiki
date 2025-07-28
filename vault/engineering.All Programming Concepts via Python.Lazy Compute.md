---
id: kqytwsfc4ah79athz7a838k
title: Lazy Compute
desc: ''
updated: 1752649788329
created: 1752649787082
---


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
